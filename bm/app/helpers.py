from app.models import Category, Bookmark

import random
import string

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

def insert_object(items, item, position=float('inf')):
	max_number = get_max_row_number(items)
	if item.row_number == max_number:
		return None
	position = min(position, max_number+1)
	for idx in items:
		if idx.row_number >= position:
			idx.row_number += 1
			idx.save()
	item.row_number = position
	item.save()

def fill_gap(items, position):
	for idx in items:
		if idx.row_number > position:
			idx.row_number -= 1
			idx.save()

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
