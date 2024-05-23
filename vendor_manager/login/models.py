from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from vendor.models import User
from rest_framework.authtoken.models import Token
from django.conf import settings


class Sessions(models.Model):
	user = models.CharField(max_length=10)

	def destroy(self):
		self.user = "None"
		self.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
