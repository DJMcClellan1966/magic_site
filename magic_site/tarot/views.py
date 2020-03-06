from django.shortcuts import render, get_object_or_404

def reading(request):
    return render(request, 'tarot/reading.html')

def question(request):
    return render(request, 'tarot/question.html')    
