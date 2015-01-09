from django.db import models
from django.conf import settings

class Category(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=21)
	row_number = models.IntegerField(default=0)
	column_number = models.IntegerField(default=0)

	def __str__(self):
		return str(self.user) + ' ' + str(self.name)

class Bookmark(models.Model):
	category = models.ForeignKey(Category)
	name = models.CharField(max_length=50)
	link = models.TextField()
	row_number = models.IntegerField(default=0)

	def __str__(self):
		return str(self.category) + ' ' + str(self.name)