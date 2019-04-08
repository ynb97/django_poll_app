# Views file for poll
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Candidate,Poll

def home(request):
	return render(request, 'poll_webapp/home.html')

def about(request):
	return render(request, 'poll_webapp/about.html', {'title': 'About'})

@login_required
def polls(request):
	context = {
		'polls_obj': Poll.objects.all()
	}
	return render(request, 'poll_webapp/polls.html', context, {'title': 'Live polls'})

def candidates(request):
	cand = {
		'cand_obj': Candidate.objects.all()
	}
	return render(request, 'poll_webapp/candidates.html', cand)