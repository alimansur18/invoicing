from django.urls import path
from .views import *
from django.contrib.auth.models import User

urlpatterns = [
    path('invoices/', Invoice.as_view(), name='invoice-get'),
    path('invoices/<int:id>/', InvoiceDetail.as_view(), name='invoice-detail'),
    path('invoices/new/', Invoice.as_view(), name='invoice-new'),
    path('user/signup/', SignUp.as_view(), name='signup'),
    path('user/signin/', SignIn.as_view(), name='signin'),
    path('invoices/<int:id>/items/', AddItems.as_view(), name='add-items'),
]
