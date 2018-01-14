from django.conf.urls import url
from django.conf import settings
from . import views

#app_name = 'catalog'
urlpatterns = [
	url('books/', views.BookListView.as_view(), name='books'),
	#url(r'^book/([0-9]+)$', views.BookDetailView.as_view(), name='book-detail'),
	url(r'^book/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='book-detail'),
	url('', views.index, name='index'),
]
