from django.urls import path, include

from . import views

urlpatterns = [
    path('letsplant', views.index, name ='index'),
    path('organization', views.Organization, name ='organization'),
    path('organizationmember', views.OrganizationMember, name ='organizationMember'),
    path('office', views.Office, name ='office'),
    path('officer', views.Officer, name ='officer'),
    path('service', views.Service, name ='service'),
    path('subscriber', views.Subscriber, name = 'subscriber'),

]
