from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Question, Answer


#class IndexView(generic.ListView):
    #template_name = 'myapp/index.html'
    #context_object_name = 'latest_question_list'

    #def get_queryset(self):
        #"""Return the last five published questions."""
        #return Question.objects.order_by('-pub_date')[:5]

resultslist = []

@login_required
def indexView(request):
    question = get_object_or_404(Question, pk=4)
    context = { 
        'question' : question,
    }
    return render(request, 'myapp/index.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'myapp/detail.html'


#@login_required
def resultsView(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # Get the next question
    next_question = Question.objects.filter(id__gt=question_id).order_by('id').first()

    context = {
        'question': question,
        'next_question': next_question,
    }

    return render(request, 'myapp/results.html', context)


#@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.answer_set.get(pk=request.POST['answer'])
        resultslist.append(selected_choice)
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        #selected_choice.save()
        selected_choice.amount += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('myapp:results', args=(question.id,)))


#@login_required 
def endView(request):
    latest_question_list = Question.objects.all()
    #combined_list = zip(latest_question_list, resultslist)
    combined_list = []

    for question, answer in zip(latest_question_list, resultslist):
        combined_list.append((question, answer))
        
    context = {
        #'latest_question_list': latest_question_list,
        #'resultslist': resultslist,
        'combined_list': combined_list,
    }
    return render(request, 'myapp/end.html', context)


class PasswordsChangingView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('myapp:index')
