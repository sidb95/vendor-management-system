from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    contact_details = models.TextField(max_length=13)
    address = models.TextField(max_length=100)
    vendor_code = models.TextField(max_length=7)
    on_time_delivery_rate = models.FloatField
    quality_rating_avg = models.FloatField
    average_response_time = models.FloatField
    fulfillment_rate = models.FloatField
