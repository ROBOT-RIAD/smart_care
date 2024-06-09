from rest_framework import serializers
from .import models

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUS
        fields ='__all__'