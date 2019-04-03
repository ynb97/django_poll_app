from django.shortcuts import render

# Views file for poll
from django.http import HttpResponse

def home(request):
	return render(request, 'poll/home.html')
