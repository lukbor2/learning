from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	content_returned = 'Rango says, Hi There World. <br> <a href="/rango/about/">Click Here for about page</a>'
	return HttpResponse(content_returned)

def about(request):
	content_returned = 'Rango says, This is the about page. <br> <a href="/rango">Back to Home Page</a>'
	return HttpResponse(content_returned)


