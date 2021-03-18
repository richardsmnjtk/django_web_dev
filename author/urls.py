from django.conf.urls import url

from . import views
 
urlpatterns = [
	url(r'^Richard$',views.Richard),
	url(r'^Christian$',views.Christian),
	
	url(r'^Pelanggan$',views.Pelanggan),
	url(r'^Crew$',views.Crew),
	url(r'^$',views.index),
	
]