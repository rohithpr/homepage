from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from app.models import Category, Bookmark, Trash
from app.predefined import *
from app.helpers import *

import app.constants as constants
import random
import string

@login_required(login_url='/b/login')
def add_ten_random_bookmarks(request):
	categories = list(Category.objects.filter(user=request.user))
	if categories == []:
		# Give a message perhaps??
		return HttpResponseRedirect('/b/edit')
	for _ in range(10):
		category = random.choice(categories)
		raw_name = list(string.ascii_lowercase)
		random.shuffle(raw_name)
		name = ''.join(raw_name[:6])
		row_number = get_max_row_number(Bookmark.objects.filter(category=category)) + 1
		if random.random() < 0.1:
			glyphicon = random.choice(constants.GLYPHICONS)
		else:
			glyphicon = ''
		bookmark = Bookmark(category=category, name=name, link=name, row_number=row_number, glyphicon=glyphicon)
		bookmark.save()
	return HttpResponseRedirect('/b/edit')

@login_required(login_url='/b/login')
def add_five_random_categories(request):
	categories = Category.objects.filter(user=request.user)
	for idx in range(5):
		raw_name = list(string.ascii_lowercase)
		random.shuffle(raw_name)
		name = ''.join(raw_name[:6])
		column_number = random.randrange(0, 6)
		row_number = get_max_row_number(categories.filter(column_number=column_number)) + 1
		progress_bar_color = get_random_color()
		category = Category(user=request.user, name=name, column_number=column_number, 
			row_number=row_number, progress_bar_color=progress_bar_color)
		category.save()
	return HttpResponseRedirect('/b/edit')

@login_required(login_url='/b/login')
def add_starter_bookmarks(request):
	old_categories = Category.objects.filter(user=request.user)
	for category in old_categories:
		category.delete()
	# Delete or not?

	for (name, column_number, row_number, progress_bar_color) in predefined_category_details:
		category = Category(user=request.user, name=name, column_number=column_number, 
			row_number=row_number, progress_bar_color=progress_bar_color)
		category.save()

	for category_name in predefined_category_names:
		category = Category.objects.filter(name=category_name)[0]
		for (name, link, row_number, glyphicon) in predefined_bookmarks[category_name]:
			bookmark = Bookmark(category=category, name=name, link=link, row_number=row_number, glyphicon=glyphicon)
			bookmark.save()

	return HttpResponseRedirect('/b/')
