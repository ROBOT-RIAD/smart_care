from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers


# Create your views here.

class ContactusViewset(viewsets.ModelViewSet):
    queryset = models.ContactUS.objects.all()
    serializer_class = serializers.ContactUsSerializer
