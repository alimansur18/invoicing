from django.urls import path
from .views import *
from django.contrib.auth.models import User

urlpatterns = [
    path('invoices/', InvoiceView.as_view(), name='All-invoice'),
    path('invoices/<int:id>/', InvoiceDetail.as_view(), name='invoice-detail'),
    path('invoices/new/', InvoiceView.as_view(), name='new-invoice'),
    path('user/signup/', SignUp.as_view(), name='signup'),
    path('user/signin/', SignIn.as_view(), name='signin'),
    path('invoices/<int:id>/items/', AddItems.as_view(), name='add-items'),
]
