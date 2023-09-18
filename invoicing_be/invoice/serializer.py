from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["desc", "rate", "quantity"]

class InvoiceSerializer(serializers.ModelSerializer):
    items=ItemSerializer(many=True)
    class Meta:
        model = Invoice
        fields = '__all__'