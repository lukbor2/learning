#urls of the contacts app

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListContactView.as_view(), name='contacts-list'),
    url(r'^new$', views.CreateContactView.as_view(), name='contacts-new'),
    ]