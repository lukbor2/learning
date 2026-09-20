from django.conf.urls import url
from django.conf import settings
from books import views
from books.views import PublisherList, PublisherDetail

app_name = 'books'

urlpatterns = [
               
    #url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', views.contact),
    url(r'^view1/$', views.view_1),
    url(r'^view2/$', views.view_2),
    url(r'^publishers/$', PublisherList.as_view()),
    url(r'^publishersdetails/(?P<pk>[0-9]+)/$', PublisherDetail.as_view()),
]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug),]
