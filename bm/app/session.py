from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']
	repassword = request.POST['repassword']
	if password != repassword:
		return HttpResponseRedirect('/b/')
	new_user = User.objects.create_user(username, password, email)
	new_user.is_active = False
	new_user.save()
	return HttpResponseRedirect('/b/inactive')
