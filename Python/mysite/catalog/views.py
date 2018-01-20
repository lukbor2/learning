from django.shortcuts import render, get_object_or_404
from django.views import generic
from catalog.models import Author, Book, BookInstance, Genre
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

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

	#Using sessions. Number of visits to this view, as counted in the session variable.
	num_visits = request.session.get('num_visits', 0) #Get the first value of num_visits
	request.session['num_visits'] = num_visits + 1

	# Render the HTML template index.html with the data in the context variable
	return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
		 'page_title': page_title, 'num_genres': num_genres, 'num_books_with_word':num_books_with_word, 'num_visits':num_visits },
    )

class BookListView(generic.ListView):
	model = Book
	paginate_by = 2 #To show 2 records per page at a time. Need to change the base html template to handle pagination.

class BookDetailView(generic.DetailView):
	model = Book

class AuthorListView(generic.ListView):
	model = Author
	paginate_by = 2

class AuthorDetailView(generic.DetailView):
	model = Author

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 2

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class AllBorrowedBooksListView(PermissionRequiredMixin, generic.ListView):
	"""
	View usable by users who have the can_mark_returned permission only.
	Lists all books which are currently on loan.
	"""
	permission_required = 'catalog.can_mark_returned'
	model = BookInstance
	template_name = 'catalog/bookinstance_list_all_borrowed_books.html'

	def get_queryset(self):
		return BookInstance.objects.filter(status__exact='o').order_by('due_back')
