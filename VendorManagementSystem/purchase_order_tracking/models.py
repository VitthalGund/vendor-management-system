from django.db import models
from vendor_management.models import Vendor
from django.utils.translation import gettext_lazy as _
import json


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    actual_delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.TextField()
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="pending")
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def set_items(self, items):
        self.items = json.dumps(items)

    def get_items(self):
        return json.loads(self.items)

    def __str__(self):
        return self.po_number
