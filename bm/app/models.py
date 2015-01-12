from django.db import models
from django.conf import settings

class Category(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=21)
	row_number = models.IntegerField(default=0)
	column_number = models.IntegerField(default=0)
	progress_bar_color = models.CharField(max_length=6, default="335544")
	# hidden = models.BooleanField(default=False)
	# trash = models.BooleanField(default=False)

	def __str__(self):
		return str(self.user) + ' ' + str(self.name)

class Bookmark(models.Model):
	category = models.ForeignKey(Category)
	name = models.CharField(max_length=50)
	link = models.TextField()
	row_number = models.IntegerField(default=0)
	glyphicon = models.CharField(max_length=30, default="asterisk")

	def __str__(self):
		return str(self.category) + ' ' + str(self.name)

class Trash(models.Model):
	category = models.ForeignKey(Category)
	name = models.CharField(max_length=50)
	link = models.TextField()
	glyphicon = models.CharField(max_length=30)

	def __str__(self):
		return str(self.category) + ' ' + str(self.name)