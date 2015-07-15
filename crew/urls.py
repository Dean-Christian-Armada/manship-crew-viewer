from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
				# url(r'^$', views.index, name='index'),
				# auto-complete-light url requirement
				url(r'^navigation_autocomplete/$', views.navigation_autocomplete, name='navigation_autocomplete'),
				url(r'^view-info/(?P<code>[a-z1-9]{4})/$', views.info, name='view-info'),
				url(r'^view-picture/(?P<code>[a-z1-9]{4})/$', views.picture, name='view-picture'),
				url(r'^view-contract/(?P<contract>(.)+)/$', views.contract, name='view-contract'),
				)