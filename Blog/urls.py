# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
	url('',TemplateView.as_view(template_name='pages/index.html'), name="index"),
	
	url(r'^blog/view/(?P<slug>[^\.]+).html',
		 TemplateView.as_view(template_name='pages/view_post.html'), name="view_post"),
		 
	url(r'blogcategory/(?P<slug>[^\.]+).html',
		TemplateView.as_view(template_name='pages/view_category.html'), name="view_category"),
		 
]