from django import forms

class OrganizationForm(forms.Form):
	orgCode = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter org code'}))
	orgName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter org name'}))
	description = forms.CharField(max_length=144, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter org description'}))
	address1 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter address1'}))
	address2 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter address2'}))
	city = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter city'}))
	state = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter state'}))
	zipcode = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter org zip code'}))
	phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter org phone'}))

class OfficeForm(forms.Form):
	officeName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Office Name'}))
	officeCode = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Office Code'}))
	attribution = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Attribution'}))


class OfficerForm(forms.Form):
	serviceCode = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Service Code'}))
	serviceName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Service Name'}))
	startDate = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Description'}))
	endDate = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Premium'}))
class SubscriberForm(forms.Form):
	subID = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Sub ID'}))
	subRequestDate = forms.DateField()
	subStartDate = forms.DateField()
	subEndDate = forms.DateField()
	cancelationReason = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Cancelation Reason'}))
	subType = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Sub Type'}))
	userName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter User Name'}))
	beneficiaryID = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter beneficiary ID'}))

class OrganizationMemberForm(forms.Form):
	membershipStart = forms.DateField()
	membershipEnd = forms.DateField()
	nativeCountry = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Native Country'}))
	citizenship = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter citizenship'}))

class ServiceForm(forms.Form):
	serviceCode = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Service Code'}))
	serviceName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Service Name'}))
	description = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Description'}))
	premium = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Premium'}))
	allocation = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class'  : 'form-control','placeholder' : 'Enter Allocation'}))
