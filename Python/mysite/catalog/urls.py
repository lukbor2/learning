from django.conf.urls import url
from django.conf import settings
from . import views

#app_name = 'catalog'
urlpatterns = [
	url('books/', views.BookListView.as_view(), name='books'),
	url(r'^book/(?P<pk>[0-9]+)$', views.BookDetailView.as_view(), name='book-detail'),
	url('authors/', views.AuthorListView.as_view(), name='authors'),
	url(r'^author/(?P<pk>[0-9]+)$', views.AuthorDetailView.as_view(), name='author-detail'),
	url('', views.index, name='index'),
]
