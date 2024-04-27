from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def purchase_order_list(request):
    if request.method == "GET":
        purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def purchase_order_detail(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(pk=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def acknowledge_purchase_order(request, po_id):
    # Retrieve the purchase order object
    purchase_order = get_object_or_404(PurchaseOrder, pk=po_id)

    # Check if the purchase order has already been acknowledged
    if purchase_order.acknowledgment_date is not None:
        return Response(
            {"error": "Purchase order has already been acknowledged."}, status=400
        )

    # Update the acknowledgment date
    purchase_order.acknowledgment_date = timezone.now()
    purchase_order.save()

    # Trigger recalculation of average response time for the vendor
    vendor = purchase_order.vendor
    vendor.calculate_performance_metrics()

    return Response(
        {"message": "Purchase order acknowledged successfully."}, status=200
    )
