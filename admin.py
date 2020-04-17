from django.contrib import admin
from .models import Subscriber, Service, Organization
# Register your models here.

admin.site.register(Subscriber)
admin.site.register(Service)
admin.site.register(Organization)