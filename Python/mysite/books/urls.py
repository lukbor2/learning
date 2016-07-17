from django.conf.urls import url
from django.conf import settings
from books import views

app_name = 'books'

urlpatterns = [
               
    #url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', views.contact),
]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug),]