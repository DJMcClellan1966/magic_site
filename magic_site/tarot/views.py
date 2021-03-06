from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.utils import timezone
from .models import Question



#@login_required(login_url = '/accounts/signup')
def question(request):
    if request.method == 'POST':
        if request.POST['question']:
            question = Question()
            question.question = request.POST['question']
            question.seeker = request.user
            question.pub_date = timezone.datetime.now()
            question.save()
            return redirect('/tarot/')
        else:
            return render(request, 'tarot/question.html',{'error': 'Need valid question'})
    else:
        return render(request, 'tarot/question.html')


def index(request):
        return render(request, 'tarot/index.html')

@login_required
def your_questions(request):
    question = Question.objects.filter(seeker=request.user)
    return render(request, 'tarot/your_questions.html', {'question':question})
