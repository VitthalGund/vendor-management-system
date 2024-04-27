from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor
from .serializers import VendorSerializer, VendorPerformanceSerializer


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
