from django.db import models

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

	def __str__(self):
		return self.name

class Office(models.Model):
	officeName = models.CharField(max_length=20)
	officeCode = models.CharField(max_length=20)
	attribution = models.CharField(max_length=20)

	def __str__(self):
		return self.officeName.officeCode.attribution

class Service(models.Model):
	serviceCode = models.CharField(max_length=20)
	serviceName = models.CharField(max_length=20)
	description = models.CharField(max_length=144)
	premium = models.CharField(max_length=20)
	allocation = models.CharField(max_length=20)

	def __str__(self):
		return self.name		

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

	def __str__(self):
		return self.name		

class Officer(models.Model):
	subID = models.CharField(max_length=20)
	officeCode = models.ForeignKey(Office, on_delete=models.CASCADE)
	startDate = models.DateField()
	endDate = models.DateField()

	def __str__(self):
		return self.name

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

	def __str__(self):
		return self.name	









