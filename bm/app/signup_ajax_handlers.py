from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

def validate_username(request):
	if request.is_ajax():
		if len(request.GET) == 0:
			return HttpResponse('1')
		for i in request.GET: # A better way to do this?
			username = i
			break
		if len(username) < 5:
			print (len(username))
			return HttpResponse('1')
		users = User.objects.filter(username=username)
		if len(users) != 0:
			# print('exists')
			return HttpResponse('1')
		else:
			# print('does not exist')
			return HttpResponse('0')

def validate_password(request):
	if request.is_ajax():
		if len(request.GET) == 0:
			return HttpResponse('1')
		for i in request.GET:
			password = i
			break
		if len(password) > 5:
			return HttpResponse('0')
		else:
			return HttpResponse('1')

def validate_email(request):
	if request.is_ajax():
		if len(request.GET) == 0:
			return HttpResponse('1')
		for i in request.GET:
			email = i
			break
		if len(email) < 1:
			return HttpResponse('1')
		users = User.objects.filter(email=email)
		if len(users) != 0:
			return HttpResponse('1')
		else:
			return HttpResponse('0')
