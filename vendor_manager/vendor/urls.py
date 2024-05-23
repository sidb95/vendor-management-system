from django.urls import path

from vendor.views import MyView

urlpatterns = [
    path("/api/vendors/", MyView.as_view(), name="vendor-view"),
]
