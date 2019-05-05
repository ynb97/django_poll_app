from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from poll_webapp.models import Poll

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for { username }! You can now login')
			return redirect('login-user')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})

# context = {
# 	'user_polls': Poll.P
# }

@login_required
def profile(request):
	return render(request, 'users/profile.html')