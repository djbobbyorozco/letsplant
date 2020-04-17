from django.shortcuts import render
from rest_framework import viewsets
from .models import Service, Organization, Subscriber
from .serializers import ServiceSerializer, OrganizationSerializer, SubscriberSerializer


class ServiceListView(viewsets.ModelViewSet): 
	queryset = Service.objects.all() 
	serializer_class = ServiceSerializer
class ServiceDetailView(viewsets.ModelViewSet): 
	queryset = Service.objects.all() 
	serializer_class = ServiceSerializer

class OrganizationListView(viewsets.ModelViewSet): 
	queryset = Organization.objects.all() 
	serializer_class = OrganizationSerializer
class OrganizationDetailView(viewsets.ModelViewSet): 
	queryset = Organization.objects.all() 
	serializer_class = OrganizationSerializer

class SubscriberListView(viewsets.ModelViewSet): 
	queryset = Subscriber.objects.all() 
	serializer_class = SubscriberSerializer
class SubscriberDetailView(viewsets.ModelViewSet): 
	queryset = Subscriber.objects.all() 
	serializer_class = SubscriberSerializer