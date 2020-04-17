from rest_framework import serializers
from .models import Subscriber, Service, Organization

class SubscriberSerializer(serializers.ModelSerializer):

	class Meta:

		model = Subscriber
		fields = ['subID', 'subRequestDate', 'subStartDate', 'subEndDate','cancelationReason', 'subType', 'userName', 'beneficiaryID']

class ServiceSerializer(serializers.ModelSerializer):

	class Meta:

		model = Service
		fields = ['serviceCode', 'serviceName', 'description', 'premium', 'allocation']

class OrganizationSerializer(serializers.ModelSerializer):

	class Meta:

		model = Organization
		fields = ['orgCode', 'description', 'address1', 'address2', 'city', 'state', 'zipcode', 'phone' ]		