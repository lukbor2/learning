from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
	url(r'^.*$', views.index, name = 'index')) # As reg-ex I could have used just ^$ too.
