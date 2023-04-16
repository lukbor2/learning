from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse, reverse_lazy
from django.template import loader
from django.template.loader import get_template
from django.template import Context

from django.utils import timezone

from .models import Question, Choice

import datetime

"""
First version of the index view. Without render.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

------------------------------------------------------------------------------

Second version of the index view was removed after introducing the generic views.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
"""

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


"""
First version of the detail view.

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

-----------------------------------------------------------------------------------

Second version of the detail view was removed after introducing the generic views.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

"""

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

"""

First version of the result view was removed after introducing the generic views.

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

"""

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

"""
First version of current_datetime view. Before using render.

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('polls/current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

"""

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'polls/current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset) #This is to convert the strin into an integer
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    # html = '<html><body>In %s hours, it will be %s .</body></html>' % (offset, dt)
    # return HttpResponse(html)
    return render(request, 'polls/hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def display_meta(request):
    values = request.META.items()
    # values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
