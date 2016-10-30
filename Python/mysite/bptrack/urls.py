from django.conf.urls import url
from django.conf import settings
from bptrack import views
# from books.views import PublisherList, PublisherDetail

app_name = 'bptrack'

urlpatterns = [
               
    #url(r'^search-form/$', views.search_form),
    url(r'^home/$', views.home),
]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug),]
