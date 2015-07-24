from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
				url(r'^$', views.home, name='home'),
				url(r'^navigation_autocomplete/$', views.navigation_autocomplete, name='navigation_autocomplete'),
				url(r'^refresh_application/', views.refresh_application, name='refresh_application'),
				url(r'^submit_application/', views.submit_application, name='submit_application'),
				)