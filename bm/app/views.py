from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from app.models import Trash
from app.helpers import *

import app.constants as constants

def inactive(request):
	return render(request, 'inactive.html')

def login_page(request):
	return render(request, 'login.html')

@login_required(login_url='/b/login')
def home_page(request):
	context = {
				'user': request.user,
				'columns': get_bookmarks(request),
	}
	return render(request, 'home.html', context)

@login_required(login_url='/b/login')
def edit_page(request):
	context = {
				'user': request.user,
				'columns': get_bookmarks(request),
				'colors': constants.COLORS,
				'glyphicons': constants.GLYPHICONS,
	}
	return render(request, 'edit2.html', context)

@login_required(login_url='/b/login')
def trash_page(request):
	bookmarks = Trash.objects.all()
	col_0 = []
	col_1 = []
	col_2 = []
	col_3 = []
	col_4 = []
	col_5 = []
	for idx in range(len(bookmarks)):
		jdx = idx + 1
		if jdx%6 == 0:
			col_5.append(bookmarks[idx])
		elif jdx%5 == 0:
			col_4.append(bookmarks[idx])
		elif jdx%4 == 0:
			col_3.append(bookmarks[idx])
		elif jdx%3 == 0:
			col_2.append(bookmarks[idx])
		elif jdx%2 == 0:
			col_1.append(bookmarks[idx])
		else:
			col_0.append(bookmarks[idx])
	columns = [col_0, col_1, col_2, col_3, col_4, col_5]
	context = {
				'columns': columns,
				'user': request.user,
	}
	return render(request, 'trash.html', context)
