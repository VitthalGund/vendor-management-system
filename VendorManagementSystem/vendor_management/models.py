from django.db import models
from django.db.models import Count, Avg, F, ExpressionWrapper, FloatField


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def calculate_performance_metrics(self):
        # Calculate on-time delivery rate
        completed_orders = self.purchaseorder_set.filter(status="completed")
        total_completed_orders = completed_orders.count()
        if total_completed_orders > 0:
            on_time_delivery_count = completed_orders.filter(
                delivery_date__lte=F("actual_delivery_date")
            ).count()
            self.on_time_delivery_rate = (
                on_time_delivery_count / total_completed_orders
            ) * 100

        # Calculate quality rating average
        self.quality_rating_avg = (
            self.purchaseorder_set.filter(quality_rating__isnull=False).aggregate(
                avg_quality=Avg("quality_rating")
            )["avg_quality"]
            or 0.0
        )

        # Calculate average response time
        response_times = (
            self.purchaseorder_set.filter(acknowledgment_date__isnull=False)
            .annotate(
                response_time=ExpressionWrapper(
                    F("acknowledgment_date") - F("issue_date"),
                    output_field=FloatField(),
                )
            )
            .aggregate(avg_response=Avg("response_time"))["avg_response"]
        )
        self.average_response_time = (
            response_times.total_seconds() if response_times else 0.0
        )

        # Calculate fulfillment rate
        total_orders = self.purchaseorder_set.count()
        if total_orders > 0:
            fulfilled_orders = self.purchaseorder_set.filter(
                status="completed", issues__isnull=True
            ).count()
            self.fulfillment_rate = (fulfilled_orders / total_orders) * 100

        self.save()

    def __str__(self):
        return self.name
