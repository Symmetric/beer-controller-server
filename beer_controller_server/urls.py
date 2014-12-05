from django.conf.urls import patterns, include, url
from django.contrib import admin
import fermentor

urlpatterns = patterns(
    '',
    url(r'^$', 'app.views.home', name='home'),
    url(r'^api/', include(fermentor.urls.urls))
)
