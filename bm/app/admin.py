from django.contrib import admin
from app.models import Category, Bookmark

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'user', 'row_number', 'column_number', 'progress_bar_color']
	list_filter = ['user']

class BookmarkAdmin(admin.ModelAdmin):
	list_display = ['category', 'name', 'row_number', 'glyphicon']
	list_filter = ['category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Bookmark, BookmarkAdmin)