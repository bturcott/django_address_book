from django.conf.urls import patterns, url
from address_book import views

urlpatterns=patterns('', 
	url(r'^$', views.index, name='address_book'),
	url(r'^add_entry/$', views.add_entry, name='add_entry'),)