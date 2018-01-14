from django.shortcuts import render, get_object_or_404
from django.views import generic
from catalog.models import Author, Book, BookInstance, Genre

def index(request):
	"""
		View function for the home page of the catalog website.
	"""

	page_title = 'Basic Library Home Page'

	#Generate counts of some of the main objects.
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()

	num_authors=Author.objects.count()  # The 'all()' is implied by default.

	#Available books
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()

	#Other Counts
	num_genres = Genre.objects.all().count()
	num_books_with_word = Book.objects.filter(title__icontains='la').count()

	# Render the HTML template index.html with the data in the context variable
	return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
		 'page_title': page_title, 'num_genres': num_genres, 'num_books_with_word':num_books_with_word },
    )

class BookListView(generic.ListView):
	model = Book

class BookDetailView(generic.DetailView):
	model = Book
