from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from .models import Customer
from .serializers import CustomerSerializer

def home(request):
     return HttpResponse("<p align='center'><h1>This is the home page.</h1></p>")
def customers(request):
    return HttpResponse("<h1>This is the customers page</h1>")

def about(request):
    return HttpResponse("<center><h1>This is the about page.</h1></center>")



class CustomerModelViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
