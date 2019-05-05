from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField

# POLL_OPTIONS = ()

class Poll(models.Model):

	title = models.CharField(max_length=50, default='dummy-poll')
	question_text = models.TextField(default='dummy-desc')
	date_posted = models.DateTimeField(default=timezone.now)
	# options = ArrayField(models.CharField(max_length=20, default='dummy-ans'),default=list('abc'))
	# options = models.CharField(max_length=128, default='a')
	# Poll_anss = models.ForeignKey(Poll_anss)

	"""docstring for Polls"""
	# def __init__(self, arg):
	# 	super(Polls, self).__init__()
	# 	self.arg = arg

		
class Poll_options(models.Model):
	question = models.ForeignKey(Poll, on_delete=models.CASCADE)
	option_text = models.CharField(max_length=28, default='a')
	# def __str__(self):
	# 	return self.option_text	


class Poll_votes(models.Model):

	ans_text = models.ForeignKey(Poll_options, on_delete=models.CASCADE)
	# poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	voter = models.ForeignKey(User, on_delete=models.CASCADE)
	date_voted = models.DateTimeField(default=timezone.now)

	"""docstring for Poll_anss"""
	# def __init__(self, arg):
	# 	super(Poll_anss, self).__init__()
	# 	self.arg = arg
	
	# def get_absolute_url(self):
	# 	return reverse('poll-vote')