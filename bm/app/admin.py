from django.contrib import admin
from app.models import Category, Bookmark, Trash, ValidationQueue

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'user', 'row_number', 'column_number', 'progress_bar_color', 'id']
	list_filter = ['user']

class BookmarkAdmin(admin.ModelAdmin):
	list_display = ['category', 'name', 'row_number', 'glyphicon', 'id']
	list_filter = ['category']

class TrashAdmin(admin.ModelAdmin):
	list_display = ['category', 'name', 'glyphicon', 'id']
	list_filter = ['category']

class ValidationQueueAdmin(admin.ModelAdmin):
	list_display = ['email', 'key']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Trash, TrashAdmin)
admin.site.register(ValidationQueue, ValidationQueueAdmin)
