from django.urls import path
from . import views

urlpatterns = [
    path("", views.purchase_order_list),
    path("<int:po_id>/", views.purchase_order_detail),
    path("<int:po_id>/acknowledge/", views.acknowledge_purchase_order),
]
