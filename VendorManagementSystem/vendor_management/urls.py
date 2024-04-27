from django.urls import path
from . import views

urlpatterns = [
    path("", views.vendor_list),
    path("<int:vendor_id>/", views.vendor_detail),
    path("<int:vendor_id>/performance/", views.vendor_performance),
    path(
        "api/purchase_orders/<int:po_id>/acknowledge/",
        views.acknowledge_purchase_order,
        name="acknowledge_purchase_order",
    ),
]
