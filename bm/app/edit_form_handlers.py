from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from app.models import Category, Bookmark
from app.helpers import *

@login_required(login_url='/b/login')
def edit_category(request):
	_id = request.POST['ID']
	category_name = request.POST['category_name']
	color = request.POST['color']
	row_number = int(request.POST['row_number'])-1
	column_number = int(request.POST['column_number'])-1
	# print(_id, category_name, color, row_number, column_number)
	category = Category.objects.get(id=_id)
	category.name = category_name
	category.progress_bar_color = color
	category.row_number = row_number
	category.column_number = column_number
	category.save()
	return HttpResponseRedirect('/b/edit/')

@login_required(login_url='/b/login')
def edit_bookmark(request):
	_id = request.POST['ID']
	bookmark_name = request.POST['bookmark_name']
	link = request.POST['link']
	category_name = request.POST['category']
	glyphicon = request.POST['glyphicon']
	row_number = max(int(request.POST['row_number'])-1, 0)

	bookmark = Bookmark.objects.get(id=_id)
	bookmark.name = bookmark_name
	bookmark.link = link
	bookmark.glyphicon = glyphicon

	try:
		category = Category.objects.get(name=category_name)
		if category == bookmark.category:
			if bookmark.row_number == row_number:
				bookmark.save()
			else:
				bookmarks = Bookmark.objects.filter(category=category)
				fill_gap(bookmarks, bookmark.row_number)
				insert_object(bookmarks, bookmark, row_number)
		else:
			bookmarks = Bookmark.objects.filter(category=bookmark.category)
			fill_gap(bookmarks, bookmark.row_number)
			bookmarks = Bookmark.objects.filter(category=category)
			insert_object(bookmarks, bookmark, row_number)
			bookmark.category = category
			bookmark.save()
	except:
		# Handle new categories
		pass
	return HttpResponseRedirect('/b/edit')
