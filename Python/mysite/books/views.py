from django.shortcuts import render
from django.http.response import HttpResponse

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submit an empty form.'
    return HttpResponse(message)