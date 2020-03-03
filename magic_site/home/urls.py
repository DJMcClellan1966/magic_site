from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('terms', views.terms, name = 'terms'),
    path('privacy', views.privacy, name = 'privacy'),
    path('home', views.home, name = 'home'),
    path('main', views.main, name = 'main'),
    path('about', views.about, name = 'about'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
