from django.shortcuts import render

def home(request):
    return render(request, 'homepage/home.html')

def main(request):
    return render(request, 'homepage/main.html')

def about(request):
    return render(request, 'homepage/about.html')    

def terms(request):
    return render(request, 'homepage/terms.html')

def privacy(request):
    return render(request, 'homepage/privacy.html')
