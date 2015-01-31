from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from app.models import Category, Bookmark
from app.helpers import *
from app.constants import COLORS

import random

@login_required(login_url='/b/login')
def add_bookmark(request, category_id):
	category = Category.objects.get(id=category_id)
	bookmarks = Bookmark.objects.filter(category=category)
	
	name = request.POST['name']
	link = request.POST['link']
	row_number = get_max_row_number(bookmarks) + 1
	bookmark = Bookmark(category=category, name=name, link=link, row_number=row_number, glyphicon='')
	bookmark.save()
	
	return HttpResponseRedirect('/b/edit')

@login_required(login_url='/b/login')
def add_category(request):
	name = request.POST['name']
	if name == '':
		return HttpResponseRedirect('/b/edit')

	color = request.POST['color']
	if color == '':
		color = random.choice(COLORS)

	column_number = request.POST['column_number']
	if column_number == '':
		column_number = random.randrange(0, 5)
	else:
		try:
			column_number = int(column_number) - 1
		except:
			column_number = random.randrange(0, 5)

	row_number = request.POST['row_number']
	if row_number == '':
		row_number = -1
	else:
		try:
			row_number = int(row_number) - 1
		except:
			row_number = -1

	category = Category(user=request.user, name=name, column_number=column_number, row_number=row_number, progress_bar_color=color)
	categories = Category.objects.filter(user=request.user).filter(column_number=column_number)
	insert_object(categories, category, row_number)
	return HttpResponseRedirect('/b/edit/')
