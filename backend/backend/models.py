from django.db import models

# Create your models here.
class Organization(models.Model):
	orgCode = models.CharField(max_length=20)
	orgName = models.CharField(max_length=20)
	description = models.CharField(max_length=144)
	address1 = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zipcode = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)
	def _str_(self):
		return self.orgCode

class Office(models.Model):
	officeName = models.CharField(max_length=20)
	officeCode = models.CharField(max_length=20)
	attribution = models.CharField(max_length=20)
	def _str_(self):
		return self.officeName.officeCode.attribution

class Service(models.Model):
	serviceCode = models.CharField(max_length=20)
	serviceName = models.CharField(max_length=20)
	description = models.CharField(max_length=144)
	premium = models.CharField(max_length=20)
	allocation = models.CharField(max_length=20)
	def _str_(self):
		return self.serviceCode

class Subscriber(models.Model):
	subID = models.CharField(max_length=20)
	serviceCode = models.ForeignKey(Service, on_delete=models.CASCADE)
	subRequestDate = models.DateField()
	subStartDate = models.DateField()
	subEndDate = models.DateField()
	cancelationReason = models.CharField(max_length=50)
	subType = models.CharField(max_length=20)
	userName = models.CharField(max_length=20)
	beneficiaryID = models.CharField(max_length=20)
	def _str_(self):
		return self.subID

class Officer(models.Model):
	subID = models.CharField(max_length=20)
	officeCode = models.ForeignKey(Office, on_delete=models.CASCADE)
	startDate = models.DateField()
	endDate = models.DateField()
	def _str_(self):
		return self.subID

class OrganizationMember(models.Model):
	orgCode = models.ForeignKey(Organization, on_delete=models.CASCADE)
	subID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
	membershipStart = models.DateField()
	membershipEnd = models.DateField()
	nativeCountry = models.CharField(max_length=20)
	citizenship = models.CharField(max_length=20)
	y = 'yes'
	n = 'no'
	delegate = (
	(y, 'yes'),
	(n, 'no')
	)
	isdelegate = models.CharField(max_length=10, choices=delegate,)
	def _str_(self):
		return self.orgCode

class UserInfo(models.Model):
	userName = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
	fName = models.CharField(max_length=20)
	mName = models.CharField(max_length=20)
	lName = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	address1 = models.CharField(max_length=20)
	address2 = models.CharField(max_length=20)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zipcode = models.CharField(max_length=20)
	empName = models.CharField(max_length=20)
	def _str_(self):
		return self.userName

class SubscriptionType(models.Model):
	subName = models.ForeignKey(Subscriber, on_delete=models.CASCADE)


class TrasferredSubscription(models.Model):
	transferID = models.CharField(max_length=20)
	transferFrom = models.CharField(max_length=20)
	transferTo = models.CharField(max_length=20)
	requestDate = models.CharField(max_length=20)
	transferDate = models.CharField(max_length=20)
	subID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)