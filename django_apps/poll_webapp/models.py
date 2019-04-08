from django.db import models
from django.utils import timezone

class Poll(models.Model):

	title = models.CharField(max_length=50, default='dummy-poll')
	poll_desc = models.TextField(default='dummy-desc')
	date_posted = models.DateTimeField(default=timezone.now)
	# candidates = models.ForeignKey(Candidates)

	"""docstring for Polls"""
	# def __init__(self, arg):
	# 	super(Polls, self).__init__()
	# 	self.arg = arg
		
class Candidate(models.Model):

	cname = models.CharField(max_length=20, default='dummy-cand')
	votes = models.IntegerField(default=0)
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

	"""docstring for Candidates"""
	# def __init__(self, arg):
	# 	super(Candidates, self).__init__()
	# 	self.arg = arg
	def __str__(self):
		return self.cname	