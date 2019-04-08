from django.contrib import admin

from .models import Poll, Candidate

admin.site.register(Poll)
admin.site.register(Candidate)