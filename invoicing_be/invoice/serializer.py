from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class InvoiceSerializer(serializers.ModelSerializer):
    items=ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Invoice
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ["name", "username", "password", "email"]
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'], 
            name = validated_data['name'],
            email = validated_data['email'], 
            password = validated_data['password'])
        return user
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")