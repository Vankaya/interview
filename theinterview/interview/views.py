from django.shortcuts import render
from django.http import  HttpResponseRedirect
from  .models import QuestionAnswer


def index(request):
    questions = QuestionAnswer.objects.all()
    return render(request, 'interview/main.html',{"questions" : questions})

def create(request):
    if request.method == 'POST':
        question=QuestionAnswer()
        question.quest = request.POST.get("quest")

        question.answ = request.POST.get("answ")
        question.save()
    return HttpResponseRedirect("/")