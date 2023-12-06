from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic

from .models import Question, Answer


#class IndexView(generic.ListView):
    #template_name = 'myapp/index.html'
    #context_object_name = 'latest_question_list'

    #def get_queryset(self):
        #"""Return the last five published questions."""
        #return Question.objects.order_by('-pub_date')[:5]



@login_required
def indexView(request):
    question = get_object_or_404(Question, pk=1)
    context = { 
        'question' : question, 
    }
    return render(request, 'myapp/index.html', context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'myapp/detail.html'

#class ResultsView(generic.DetailView):
    #model = Question
    #template_name = 'myapp/results.html'

def resultsView(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # Get the next question
    next_question = Question.objects.filter(id__gt=question_id).order_by('id').first()

    context = {
        'question': question,
        'next_question': next_question,
    }

    return render(request, 'myapp/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.save()
        #selected_choice.votes += 1
        #selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('myapp:results', args=(question.id)))
