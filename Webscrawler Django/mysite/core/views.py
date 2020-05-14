from django.shortcuts import render,redirect
from django.contrib.auth.models import User

#importing made form from django github
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth.decorators import login_required

def home(request):
	count = User.objects.count()
	return render(request,'home.html',{
		'count':count
		})

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()	
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request,'registration/signup.html',{
		'form':form
		})

#to make sure that secret can't be accessed without logging in first
@login_required
def secret(request):
	return render(request,'secret.html')
