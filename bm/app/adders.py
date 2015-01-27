from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from app.models import Category, Bookmark
from app.helpers import get_max_row_number

@login_required(login_url='/b/login')
def add_bookmark(request, category_id):
	category = Category.objects.get(id=category_id)
	bookmarks = Bookmark.objects.filter(category=category)
	
	name = request.POST['name']
	link = request.POST['link']
	row_number = get_max_row_number(bookmarks)
	bookmark = Bookmark(category=category, name=name, link=link, row_number=row_number, glyphicon='')
	bookmark.save()
	
	return HttpResponseRedirect('/b/edit')
