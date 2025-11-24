from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
# Create your views here.
def home(request):
     return HttpResponse("<p align='center'><h1>This is the about page.</h1></p>")
def customers(request):
    return HttpResponse("<h1>This is the customers page</h1>")

def about(request):
    return HttpResponse("<center><h1>This is the about page.</h1></center>")


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
