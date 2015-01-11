from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from app.models import Category, Bookmark

import random
import string

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

GLYPHICONS = ['asterisk', 'plus', 'minus', 'euro', 'cloud', 'envelope', 'pencil', 'glass', 'music', 'search',
			  'heart', 'star', 'star-empty', 'user', 'film', 'th-large', 'th', 'th-list', 'ok', 'remove',
			  'off', 'cog', 'home', 'file', 'time', 'road', 'download', 'upload', 'inbox', 'play-circle', 
			  'repeat', 'refresh', 'lock', 'flag', 'headphones', 'tag', 'tags', 'book', 'bookmark', 'print',
			  'camera', 'facetime-video', 'picture', 'map-marker', 'tint', 'edit', 'play', 'pause', 'stop',
			  'chevron-up', 'chevron-down', 'chevron-left', 'chevron-right', 'plus-sign', 'minus-sign', 'remove-sign',
			  'ok-sign', 'question-sign', 'leaf', 'fire', 'plane', 'magnet', 'comment', 'shopping-cart', 'bullhorn',
			  'bell', 'certificate', 'globe', 'wrench', 'filter', 'heart-empty', 'phone', 'pushpin', 'gbp', 'usd',
			  'flash', 'record', 'send', 'cutlery', 'earphone', 'phone-alt', 'tower', 'tree-conifer', 'tree-deciduos', '',
]

def get_bookmarks(request):
	categories = Category.objects.filter(user=request.user)
	# 6 columns only
	raw_col_0 = categories.filter(column_number=0).order_by('row_number')
	col_0 = []
	for category in raw_col_0:
		col_0.append([category, Bookmark.objects.filter(category=category).order_by('row_number')])

	raw_col_1 = categories.filter(column_number=1).order_by('row_number')
	col_1 = []
	for category in raw_col_1:
		col_1.append([category, Bookmark.objects.filter(category=category).order_by('row_number')])
	
	raw_col_2 = categories.filter(column_number=2).order_by('row_number')
	col_2 = []
	for category in raw_col_2:
		col_2.append([category, Bookmark.objects.filter(category=category).order_by('row_number')])
	
	raw_col_3 = categories.filter(column_number=3).order_by('row_number')
	col_3 = []
	for category in raw_col_3:
		col_3.append([category, Bookmark.objects.filter(category=category).order_by('row_number')])
	
	raw_col_4 = categories.filter(column_number=4).order_by('row_number')
	col_4 = []
	for category in raw_col_4:
		col_4.append([category, Bookmark.objects.filter(category=category).order_by('row_number')])
	
	raw_col_5 = categories.filter(column_number=5).order_by('row_number')
	col_5 = []
	for category in raw_col_5:
		col_5.append([category, Bookmark.objects.filter(category=category).order_by('row_number')])

	return [col_0, col_1, col_2, col_3, col_4, col_5]

def get_max_row_number(items):
	max_num = -1
	for item in items:
		if item.row_number > max_num:
			max_num = item.row_number
	return max_num

def get_random_color():
	hexdigits = list(string.hexdigits * 6)
	random.shuffle(hexdigits)
	return ''.join(hexdigits[:6])

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

@login_required(login_url='/b/login')
def edit_page(request):
	context = {
				'user': request.user,
				'columns': get_bookmarks(request),
			}
	return render(request, 'edit2.html', context)

@login_required(login_url='/b/login')
def bookmark_up(request, bookmark_id):
	current = Bookmark.objects.get(id=bookmark_id)
	if current.row_number != 0: # If its the first bookmark in that category it can't be moved up further.
		previous = Bookmark.objects.filter(category=current.category).get(row_number=current.row_number-1)
		previous.row_number += 1
		current.row_number -= 1
		previous.save()
		current.save()
	return HttpResponseRedirect('/b/edit')

@login_required(login_url='/b/login')
def bookmark_down(request, bookmark_id):
	current = Bookmark.objects.get(id=bookmark_id)
	try: # If its the last bookmark in that category it can't be moved down further.
		following = Bookmark.objects.filter(category=current.category).get(row_number=current.row_number+1)
		following.row_number -= 1
		current.row_number += 1
		following.save()
		current.save()
	except:
		pass
	return HttpResponseRedirect('/b/edit')

@login_required(login_url='/b/login')
def delete_bookmark(request, bookmark_id):
	current = Bookmark.objects.get(id=bookmark_id)
	following = Bookmark.objects.filter(category=current.category).filter(row_number__gt=current.row_number)
	for idx in following:
		idx.row_number -= 1
		idx.save()
	current.delete()
	return HttpResponseRedirect('/b/edit')

@login_required(login_url='/b/login')
def category_up(request, category_id):
	current = Category.objects.get(id=category_id)
	if current.row_number != 0:
		previous = Category.objects.filter(user=request.user)
		previous = previous.filter(column_number=current.column_number).get(row_number=current.row_number-1)
		previous.row_number += 1
		current.row_number -= 1
		previous.save()
		current.save()
	return HttpResponseRedirect('/b/edit')
	
@login_required(login_url='/b/login')
def category_down(request, category_id):
	current = Category.objects.get(id=category_id)
	try:
		following = Category.objects.filter(user=request.user)
		following = following.filter(column_number=current.column_number).get(row_number=current.row_number+1)
		following.row_number -= 1
		current.row_number += 1
		following.save()
		current.save()
	except:
		pass
	return HttpResponseRedirect('/b/edit')
	# return HttpResponse(str(current))

@login_required(login_url='/b/login')
def category_left(request, category_id):
	current = Category.objects.get(id=category_id)
	if current.column_number != 0:
		user_categories = Category.objects.filter(user=request.user)
		below = user_categories.filter(column_number=current.column_number).filter(row_number__gt=current.row_number)
		                                           # Move stuff up to fill the hole
		previous = user_categories.filter(column_number=current.column_number-1)

		max_number = get_max_row_number(previous)
		if max_number >= current.row_number:        # If it has more rows then insert.
			previous = previous.filter(row_number__gte=current.row_number)
			for idx in previous:                  # Make space for the category in the new column
				idx.row_number += 1
				idx.save()
		else:                                      # If it has lesser rows then append
			current.row_number = max_number + 1

		for idx in below:
			idx.row_number -= 1
			idx.save()
		
		current.column_number -= 1
		current.save()
	return HttpResponseRedirect('/b/edit')

@login_required(login_url='/b/login')
def category_right(request, category_id):
	current = Category.objects.get(id=category_id)
	if current.column_number != 5:
		user_categories = Category.objects.filter(user=request.user)
		below = user_categories.filter(column_number=current.column_number).filter(row_number__gt=current.row_number)
		                                           # Move stuff up to fill the hole
		following = user_categories.filter(column_number=current.column_number+1)

		max_number = get_max_row_number(following)
		if max_number >= current.row_number:        # If it has more rows then insert.
			following = following.filter(row_number__gte=current.row_number)
			for idx in following:                  # Make space for the category in the new column
				idx.row_number += 1
				idx.save()
		else:                                      # If it has lesser rows then append
			current.row_number = max_number + 1

		for idx in below:
			idx.row_number -= 1
			idx.save()
		
		current.column_number += 1
		current.save()
	return HttpResponseRedirect('/b/edit')

@login_required(login_url='/b/login')
def random_color(request, category_id):
	current = Category.objects.get(id=category_id)
	current.progress_bar_color = get_random_color()
	current.save()
	return HttpResponseRedirect('/b/edit')

@login_required(login_url='/b/login')
def random_glyphicon(request, bookmark_id):
	current = Bookmark.objects.get(id=bookmark_id)
	current.glyphicon = random.choice(GLYPHICONS)
	current.save()
	return HttpResponseRedirect('/b/edit')

@login_required(login_url='/b/login')
def add_ten_random_bookmarks(request):
	categories = list(Category.objects.filter(user=request.user))
	for _ in range(10):
		category = random.choice(categories)
		raw_name = list(string.ascii_lowercase)
		random.shuffle(raw_name)
		name = ''.join(raw_name[:6])
		link = ''.join(raw_name[-6:])
		row_number = get_max_row_number(Bookmark.objects.filter(category=category)) + 1
		glyphicon = random.choice(GLYPHICONS)
		bookmark = Bookmark(category=category, name=name, link=link, row_number=row_number, glyphicon=glyphicon)
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
