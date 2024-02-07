from rest_framework import serializers
from .models import *

#contact us
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
