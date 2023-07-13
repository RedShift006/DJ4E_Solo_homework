from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404
# Create your views here.

# def index(request):
#     return HttpResponse("<p>Answer to the Ultimate Question</p>")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def owner(request):
   return HttpResponse("Hello, world. 8f8161d3 is the polls index.")

def detail(request, question_id):
    one_question = get_object_or_404(Question, id=question_id)
    return HttpResponse("Your Question is %s. You're looking at question %s." %(one_question, question_id))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
