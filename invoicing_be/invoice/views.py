from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .data import *
from .serializer import *
import uuid
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated 

# Create your views here.

class InvoiceView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        invoices = Invoice.objects.filter(user=request.user.id)
        serializer = InvoiceSerializer(invoices, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    def post(self, request):
        invoice_data = request.data
        invoice_data['user'] = request.user.id
        serializer = InvoiceSerializer(data=invoice_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Invoice Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        invoice = Invoice.objects.get(user=request.user.id, invoice_id=id)
        serializer = InvoiceSerializer(invoice).data
        return Response(serializer, status=status.HTTP_200_OK)
    
class AddItems(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, id):
        item_data = request.data
        item_data["invoice"] = id
        serializer = ItemSerializer(data=item_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Item Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class SignUp(APIView):
    def post(self, request):
        user_data = request.data
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SignIn(APIView):
    def post(self, request):
        user_data = request.data
        serializer = LoginSerializer(data=user_data)
        if serializer.is_valid():
            user = serializer.validated_data
            token = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "Login Successful", 
                    "access_token": str(token.access_token),
                    "refresh_token": str(token),
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    