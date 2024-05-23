from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from vendor.models import User


class VendorView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")
    
    def index(self):
        users = User.objects.all()
        for i in range (0, len(users)):
            pass


