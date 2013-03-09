'''
Created on Mar 9, 2013

@author: Hasil
'''
from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^$','blog.apps.homepage.views.index'),
                       
                       )