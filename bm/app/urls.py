from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
	url('^$', views.home_page),
	url('^login/', views.login_page),
	url('^verify/', views.verify),
	url('^logout/', views.logout_page)
	)