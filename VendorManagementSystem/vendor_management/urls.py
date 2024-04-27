from django.urls import path
from . import views

urlpatterns = [
    path("", views.vendor_list),
    path("<int:vendor_id>/", views.vendor_detail),
    path("<int:vendor_id>/performance/", views.vendor_performance),
]
