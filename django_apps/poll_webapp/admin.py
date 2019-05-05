from django.contrib import admin

from .models import Poll, Poll_options

admin.site.register(Poll)
admin.site.register(Poll_options)