from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='poll-home'),
    path('polls', views.polls, name='poll-polls'),
    path('about', views.about, name='poll-about'),
    path('candidates', views.candidates, name='poll-candidates'),
]