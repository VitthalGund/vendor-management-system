from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor, HistoricalPerformance
from .serializers import (
    VendorSerializer,
    VendorPerformanceSerializer,
    HistoricalPerformanceSerializer,
)
from django.utils import timezone
from django.shortcuts import get_object_or_404
from purchase_order_tracking.models import PurchaseOrder
from purchase_order_tracking.serializers import PurchaseOrderSerializer


@api_view(["GET", "POST"])
def vendor_list(request):
    if request.method == "GET":
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def vendor_detail(request, vendor_id):
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return Response({"message": "Not found!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def vendor_performance(request, vendor_id):
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    vendor.calculate_performance_metrics()  # Ensure performance metrics are up-to-date
    serializer = VendorPerformanceSerializer(vendor)
    return Response(serializer.data)


@api_view(["GET"])
def vendor_historical_performance(request, vendor_id):
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    historical_data = HistoricalPerformance.objects.filter(vendor=vendor).order_by(
        "-date"
    )
    serializer = HistoricalPerformanceSerializer(historical_data, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def acknowledge_purchase_order(request, po_id):
    # Retrieve the purchase order
    purchase_order = get_object_or_404(PurchaseOrder, id=po_id)

    # Check if the vendor is authenticated and authorized to acknowledge the purchase order
    # Implement authentication logic here

    # Update acknowledgment date to current timestamp
    purchase_order.acknowledgment_date = timezone.now()
    purchase_order.save()

    # Trigger recalculation of average response time for the vendor
    purchase_order.vendor.calculate_performance_metrics()

    # Serialize the updated purchase order
    serializer = PurchaseOrderSerializer(purchase_order)

    return Response(serializer.data, status=status.HTTP_200_OK)
