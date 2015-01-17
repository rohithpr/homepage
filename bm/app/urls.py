from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
	url('^login/', views.login_page),
	url('^verify/', views.verify),
	url('^logout/', views.logout_page),

	url('^$', views.home_page),
	url('^edit/', views.edit_page),
	url('^trash/', views.trash_page),

	url('^bookmark_up/(?P<bookmark_id>\d+)', views.bookmark_up),
	url('^bookmark_down/(?P<bookmark_id>\d+)', views.bookmark_down),

	url('^category_up/(?P<category_id>\d+)', views.category_up),
	url('^category_down/(?P<category_id>\d+)', views.category_down),
	url('^category_left/(?P<category_id>\d+)', views.category_left),
	url('^category_right/(?P<category_id>\d+)', views.category_right),
	
	url('^random_glyphicon/(?P<bookmark_id>\d+)', views.random_glyphicon),
	url('^random_color/(?P<category_id>\d+)', views.random_color),

	url('^trash_bookmark/(?P<bookmark_id>\d+)', views.trash_bookmark),
	url('^delete_bookmark/(?P<bookmark_id>\d+)', views.delete_bookmark),
	url('^restore_bookmark/(?P<bookmark_id>\d+)', views.restore_bookmark),
	url('^clear_trash', views.clear_trash),
	url('^delete_category/(?P<category_id>\d+)', views.delete_category),

	url('^add_ten_random_bookmarks/', views.add_ten_random_bookmarks),
	url('^add_five_random_categories/', views.add_five_random_categories),
	)