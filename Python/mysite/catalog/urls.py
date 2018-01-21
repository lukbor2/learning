from django.conf.urls import url
from django.conf import settings
from . import views

#app_name = 'catalog'
urlpatterns = [
	url(r'^books/$', views.BookListView.as_view(), name='books'),
	url(r'^book/(?P<pk>[0-9]+)$', views.BookDetailView.as_view(), name='book-detail'),
	url('book/create/', views.BookCreate.as_view(), name='book-create'),
	url(r'^book/(?P<pk>[0-9]+)/update/$', views.BookUpdate.as_view(), name='book-update'),
	url(r'^book/(?P<pk>[0-9]+)/delete/$', views.BookDelete.as_view(), name='book-delete'),
	url('authors/', views.AuthorListView.as_view(), name='authors'),
	url('author/create/', views.AuthorCreate.as_view(), name='author-create'),
	url(r'^author/(?P<pk>[0-9]+)/update/$', views.AuthorUpdate.as_view(), name='author-update'),
	url(r'^author/(?P<pk>[0-9]+)/delete/$', views.AuthorDelete.as_view(), name='author-delete'),
	url(r'^author/(?P<pk>[0-9]+)$', views.AuthorDetailView.as_view(), name='author-detail'),
	url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
	url(r'^allborrowedbooks/$', views.AllBorrowedBooksListView.as_view(), name='all-borrowed-books'),
	url(r'^book/(?P<pk>[0-9a-f-]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
	url('', views.index, name='index'),
]
