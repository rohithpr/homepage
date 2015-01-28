from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.helpers import create_validator
from app.models import ValidationQueue

def verify(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/b/login/')
	else:
		return HttpResponseRedirect('/b/login/')

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

def add_user(request):
	# Check if username or email exists
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']
	repassword = request.POST['repassword']
	if password != repassword:
		return HttpResponseRedirect('/b/')
	new_user = User.objects.create_user(username=username, password=password, email=email)
	new_user.is_active = False
	new_user.save()

	create_validator(email)

	return HttpResponseRedirect('/b/inactive')

def confirm_account(request, key):
	validator = ValidationQueue.objects.get(key=key)
	user = User.objects.get(email=validator.email)
	user.is_active = True
	user.save()
	validator.delete()
	# user = authenticate(username=user.username, password=user.password)
	user.backend = 'django.contrib.auth.backends.ModelBackend'
	login(request, user)
	return HttpResponseRedirect('/b/delete_existing_and_add_default_bookmarks/')
