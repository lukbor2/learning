from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

from bptrack.models import Patient, BP_Measure


def home(request):
    return render(request, 'bptrack_home.html')


def debug(request):
    pass

