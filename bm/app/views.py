from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from app.models import Category, Bookmark

@login_required(login_url='/b/login')
def home_page(request):
	categories = Category.objects.filter(user=request.user)
	bookmarks = {}
	for category in categories:
		bookmarks[category] = Bookmark.objects.filter(category=category)

	context = {'user': request.user, 'categories': categories, 'bookmarks': bookmarks}
	# print(context)
	return render(request, 'home.html', context)

def login_page(request):
	return render(request, 'login.html')

def verify(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			print("*** Logged in: ", user)
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/b/login/')

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')