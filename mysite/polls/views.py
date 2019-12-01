from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Question
from django.template import loader


# Create your views here.

# def index(request):
#
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list': latest_question_list}
#     return HttpResponse(template.render(context, request))

def index(request):
    """ новый index нваисанный с помощью render"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     """ вы видите опрос """
#     return HttpResponse(f"You're looking at question {question_id}.")

# def detail(request, question_id):
#     """ вариант без сокращения"""
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


from django.shortcuts import get_object_or_404


def detail(request, question_id):
    """ вариант c сокращением"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def result(request, question_id):
    """ вы видите результат опроса """
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
