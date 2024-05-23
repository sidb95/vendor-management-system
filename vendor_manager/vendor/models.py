from django.db import models
from rest_framework.authtoken.models import Token

class User(models.Model):

    def __init__(self, *args, **kwargs):
        name = models.CharField(max_length=30)
        contact_details = models.TextField(max_length=13)
        address = models.TextField(max_length=100)
        vendor_code = Token.objects.create(self)
        on_time_delivery_rate = models.FloatField
        quality_rating_avg = models.FloatField
        average_response_time = models.FloatField
        fulfillment_rate = models.FloatField
