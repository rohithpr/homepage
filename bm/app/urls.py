from django.conf.urls import patterns, url
from app import views, actions, bulk_adders, edit_form_handlers, session, adders, test
from app import signup_ajax_handlers

urlpatterns = patterns('',
	url('^login/', views.login_page),  # This must be a part of views and not session.
	url('^inactive/', views.inactive),
	url('^verify/', session.verify),
	url('^logout/', session.logout_page),
	url('^add_user/', session.add_user),
	url('^confirm_account/(?P<key>\w+)/$', session.confirm_account),

	url('^$', views.home_page),
	url('^edit/', views.edit_page),
	url('^trash/', views.trash_page),

	url('^bookmark_up/(?P<bookmark_id>\d+)', actions.bookmark_up),
	url('^bookmark_down/(?P<bookmark_id>\d+)', actions.bookmark_down),

	url('^category_up/(?P<category_id>\d+)', actions.category_up),
	url('^category_down/(?P<category_id>\d+)', actions.category_down),
	url('^category_left/(?P<category_id>\d+)', actions.category_left),
	url('^category_right/(?P<category_id>\d+)', actions.category_right),
	
	url('^random_glyphicon/(?P<bookmark_id>\d+)', actions.random_glyphicon),
	url('^random_color/(?P<category_id>\d+)', actions.random_color),

	url('^trash_bookmark/(?P<bookmark_id>\d+)', actions.trash_bookmark),
	url('^delete_bookmark/(?P<bookmark_id>\d+)', actions.delete_bookmark),
	url('^restore_bookmark/(?P<bookmark_id>\d+)', actions.restore_bookmark),
	url('^clear_trash', actions.clear_trash),
	url('^delete_category/(?P<category_id>\d+)', actions.delete_category),

	url('^add_ten_random_bookmarks/', bulk_adders.add_ten_random_bookmarks),
	url('^add_five_random_categories/', bulk_adders.add_five_random_categories),
	url('^delete_existing_and_add_default_bookmarks/', bulk_adders.add_starter_bookmarks),

	url('^add_bookmark/(?P<category_id>\d+)', adders.add_bookmark),

	url('^edit_category/', edit_form_handlers.edit_category),
	url('^edit_bookmark/', edit_form_handlers.edit_bookmark),

	url('^is_duplicate_username/', signup_ajax_handlers.validate_username),
	url('^is_valid_password/', signup_ajax_handlers.validate_password),
	url('^is_duplicate_email/', signup_ajax_handlers.validate_email),

	url('^test/', test.test),
	)