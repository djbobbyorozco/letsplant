from django.shortcuts import render, redirect

from .models import Organization
from .forms import OrganizationForm
from .forms import OrganizationMemberForm
from .forms import OfficeForm
from .forms import OfficerForm
from .forms import SubscriberForm
from .forms import ServiceForm

def index(request):
	return render(request,'letsplant/index.html')

def Organization(request):
	if request.method == 'POST':
		form = OrganizationForm(request.POST)

		if form.is_valid():
			new_organization = OrganizationForm(orgCode=request.POST['orgCode'], orgName=request.POST['orgName'], 
				description=request.POST['description'], address1=request.POST['address1'], 
				address2=request.POST['address1'], city=request.POST['city'], state=request.POST['state'], zipcode=request.POST['zipcode'], phone=request.POST['phone'])
			new_organization.save()
			return redirect('index')
	else:
		form = OrganizationForm()

	context = {'form' : form}
	return render(request, 'letsplant/organization.html', context)

def OrganizationMember(request):
	if request.method == 'POST':
		form = OrganizationMemberForm(request.POST)

		if form.is_valid():
			new_organization_member = OrganizationMemberForm(membershipDate=request.POST['membershipDate'], membershipEnd=request.POST['membershipEnd'], 
				nativeCountry=request.POST['nativeCountry'], citizenship=request.POST['citizenship'])
			new_organization.save()
			return redirect('index')
	else:
		form = OrganizationMemberForm()

	context = {'form' : form}
	return render(request, 'letsplant/organizationmember.html', context)

def Office(request):
	if request.method == 'POST':
		form = OfficeForm(request.POST)

		if form.is_valid():
			new_office = OfficeForm(officeName=request.POST['officeName'], officeCode=request.POST['officeCode'], 
				attribution=request.POST['attribution'])
			new_office.save()
			return redirect('index')
	else:
		form = OfficeForm()

	context = {'form' : form}
	return render(request, 'letsplant/office.html', context)	

def Officer(request):
	if request.method == 'POST':
		form = OfficerForm(request.POST)

		if form.is_valid():
			new_officer = OfficerForm(serviceCode=request.POST['serviceCode'], serviceName=request.POST['serviceName'], 
				startDate=request.POST['startDate'], endDate=request.POST['endDate'])
			new_officer.save()
			return redirect('index')
	else:
		form = OfficerForm()

	context = {'form' : form}
	return render(request, 'lets/plantofficer.html', context)	

def Service(request):
	if request.method == 'POST':
		form = ServiceForm(request.POST)

		if form.is_valid():
			new_service = ServiceForm(serviceCode=request.POST['serviceCode'], serviceName=request.POST['serviceName'], 
				description=request.POST['description'], premium=request.POST['premium'], allocation=request.POST['allocation'])
			new_service.save()
			return redirect('index')
	else:
		form = ServiceForm()

	context = {'form' : form}
	return render(request, 'letsplant/service.html', context)	

def Subscriber(request):
	if request.method == 'POST':
		form = SubscriberForm(request.POST)

		if form.is_valid():
			new_office = SubscriberForm(subID=request.POST['subID'], subRequestDate=request.POST['subRequestDate'], 
				subStartDate=request.POST['subStartDate'], subEndDate=request.POST['subEndDate'], 
				cancelationReason=request.POST['cancelationReason'], subType=request.POST['subType'],userName=request.POST['userName'],
				beneficiaryID=request.POST['beneficiaryID'])
			new_Subscriber.save()
			return redirect('index')
	else:
		form = SubscriberForm()

	context = {'form' : form}
	return render(request, 'lets/plantsubscriber.html', context)			
	