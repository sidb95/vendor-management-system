from django.urls import path

from vendor.views import VendorView

urlpatterns = [
    path("/api/vendors/", VendorView.as_view(), name="index"),
]
