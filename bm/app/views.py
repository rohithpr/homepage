from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from app.models import Category, Bookmark

############################################################
# SESSION STUFF
############################################################

def login_page(request):
	return render(request, 'login.html')

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

############################################################
# HELPERS
############################################################

def get_bookmarks(request):
	categories = Category.objects.filter(user=request.user)
	# 6 columns only
	raw_col_0 = categories.filter(column_number=0).order_by('row_number')
	col_0 = []
	for category in raw_col_0:
		col_0.append([category, Bookmark.objects.filter(category=category)])

	raw_col_1 = categories.filter(column_number=1).order_by('row_number')
	col_1 = []
	for category in raw_col_1:
		col_1.append([category, Bookmark.objects.filter(category=category)])
	
	raw_col_2 = categories.filter(column_number=2).order_by('row_number')
	col_2 = []
	for category in raw_col_2:
		col_2.append([category, Bookmark.objects.filter(category=category)])
	
	raw_col_3 = categories.filter(column_number=3).order_by('row_number')
	col_3 = []
	for category in raw_col_3:
		col_3.append([category, Bookmark.objects.filter(category=category)])
	
	raw_col_4 = categories.filter(column_number=4).order_by('row_number')
	col_4 = []
	for category in raw_col_4:
		col_4.append([category, Bookmark.objects.filter(category=category)])
	
	raw_col_5 = categories.filter(column_number=5).order_by('row_number')
	col_5 = []
	for category in raw_col_5:
		col_5.append([category, Bookmark.objects.filter(category=category)])

	return [col_0, col_1, col_2, col_3, col_4, col_5]

############################################################
# MAIN
############################################################

@login_required(login_url='/b/login')
def home_page(request):
	context = {
				'user': request.user,
				'columns': get_bookmarks(request),
			}
	return render(request, 'home.html', context)
