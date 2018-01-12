from django.shortcuts import render
from models import Author, Book, BookInstance, Genre

def index(request):
	"""
		View function for the home page of the catalog website.
	"""
	#Generate counts of some of the main objects.
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	
	num_authors=Author.objects.count()  # The 'all()' is implied by default.

	#Available books
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	
	# Render the HTML template index.html with the data in the context variable
	return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )