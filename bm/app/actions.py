from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect

from app.models import Category, Bookmark, Trash
from app.helpers import *

import app.constants as constants
import random

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
def trash_bookmark(request, bookmark_id): # Moves to trash!
	current = Bookmark.objects.get(id=bookmark_id)
	following = Bookmark.objects.filter(category=current.category).filter(row_number__gt=current.row_number)
	for idx in following:
		idx.row_number -= 1
		idx.save()
	bookmark = Trash(category=current.category, name=current.name, link=current.link, glyphicon=current.glyphicon)
	bookmark.save()
	current.delete()
	return HttpResponseRedirect('/b/edit')

@login_required(login_url='/b/login')
def restore_bookmark(request, bookmark_id): # Moves back to bookmarks!
	print(bookmark_id)
	current = Trash.objects.get(id=bookmark_id)
	bookmarks = Bookmark.objects.filter(category=current.category)
	row_number = get_max_row_number(bookmarks) + 1
	bookmark = Bookmark(category=current.category, name=current.name, link=current.link, 
		row_number=row_number, glyphicon=current.glyphicon)
	bookmark.save()
	current.delete()
	return HttpResponseRedirect('/b/trash')

@login_required(login_url='/b/login')
def delete_bookmark(request, bookmark_id): # Deletes from trash, no more recovery options.
	current = Trash.objects.get(id=bookmark_id)
	current.delete()
	return HttpResponseRedirect('/b/trash')

@login_required(login_url='/b/login')
def clear_trash(request):
	current = Trash.objects.all()
	for idx in current:
		idx.delete()
	return HttpResponseRedirect('/')

@login_required(login_url='/b/login')
def delete_category(request, category_id): # No recovery.
	current = Category.objects.get(id=category_id)
	below = Category.objects.filter(user=request.user).filter(column_number=current.column_number)
	below = below.filter(row_number__gt=current.row_number)
	for idx in below:
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
	current.glyphicon = random.choice(constants.GLYPHICONS)
	current.save()
	return HttpResponseRedirect('/b/edit')
