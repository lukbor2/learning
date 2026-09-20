from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from books.forms import ContactForm
from django.core.mail import send_mail
from django.template import RequestContext

from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Publisher, Book

"""

def search_form(request):
    return render(request, 'search_form.html')

"""

def debug(request):
    pass

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                      cd['subject'],
                      cd['message'],
                      cd.get('email', 'noreply@example.com'),
                      ['siteowner@example.com'],
                      ) 
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
                initial={'subject': 'I love this site!'}
            )
    return render(request, 'contact_form.html', {'form': form})

def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'"
    return {
        'app': 'books',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
        }
    
def view_1(request):
    return render(request, 'template1.html', {'message': 'I am view 1.'}, context_instance=RequestContext(request, processors=[custom_proc]))


def view_2(request):
    return render(request, 'template2.html', {'message': 'I am view 2.', 'somevariable': 'A100B200C3'}, context_instance=RequestContext(request, processors=[custom_proc]))

#example of a generic view
class PublisherList(ListView):
    model = Publisher
    # line below to provide a friendly context object rather than the standard object_list
    context_object_name = 'list_of_publishers'

#another generic view but adding extra context
#look at the url config to call this view, it requires to use pk
#so an example of the url would be http://127.0.0.1:8000/books/publishersdetails/1/
class PublisherDetail(DetailView):
	model = Publisher

	def get_context_data(self, **kwargs):
		#call base implementation first to get a context
		context = super(PublisherDetail, self).get_context_data(**kwargs)
		
		#Add queryset of all the books
		context['book_list'] = Book.objects.filter(publisher=pk)
		return context

