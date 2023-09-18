from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .data import *
from .serializer import *
import uuid

# Create your views here.

class Invoice(APIView):
    def get(self, request):
        serializer = InvoiceSerializer(invoices, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    def post(self, request):
        invoice_data = request.data
        invoice_data["invoice_id"] = len(invoices) + 1 
        serializer = InvoiceSerializer(data=invoice_data)
        if serializer.is_valid():
            invoices.append(serializer.data)
            return Response({"message": "Invoice Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceDetail(APIView):
    def get(self, request, id):
        for each in invoices:
            if each['invoice_id'] == id:
                serializer = InvoiceSerializer(each).data
                return Response(serializer, status=status.HTTP_200_OK)
        return Response({"message": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
    
class AddItems(APIView):
    def post(self, request, id):
            for each in invoices:
                if each['invoice_id'] == id:
                    item_data = request.data
                    serializer = ItemSerializer(data=item_data)
                    if serializer.is_valid():
                        each['items'].append(serializer.data)
                        return Response({"message": "Item Created"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
            return Response({"message": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
    
class SignUp(APIView):
    def post(self, request):
        user_data = request.data
        user_data["user_id"] = len(user) + 1 
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            user.append(serializer.data)
            return Response({"message": "Account Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SignIn(APIView):
    def post(self, request):
        user_data = request.data
        for each in user:
            if each['email'] == user_data['email'] and each['password'] == user_data['password']:
                return Response({"message": "Login Successful", "token": str(uuid.uuid4())}, status=status.HTTP_200_OK)
        return Response({"message": "Email or Password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)    