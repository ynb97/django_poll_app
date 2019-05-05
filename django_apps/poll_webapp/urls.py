from django.conf.urls import url
from django.urls import path
from .views import (
	PollListView,
	PollDetailView,
    ResultListView
	# Poll_votesCreateView
)
from . import views

# app_name='poll_webapp'
urlpatterns = [
    path('', PollListView.as_view(), name='poll-home'),
    path('polls', PollListView.as_view(), name='poll-polls'),
    path('polls/<int:pk>/', PollDetailView.as_view(), name='poll-detail'),
    path('about', views.about, name='poll-about'),
    path('results', ResultListView.as_view(), name='poll-result'),
    url(r'^(?P<poll_id>[0-9]+)/vote/', views.vote, name='poll-vote'),
    # path('candidates', views.candidates, name='poll-candidates'),
]
    # path(r'^(?P<poll_id>[0-9]+)/vote/$', views.vote, name='poll-vote'),
    # path('vote', Poll_votesCreateView.as_view(), name='poll-vote'),