
from django.contrib import admin
from django.conf.urls import url, include    

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^organisasi/',include('organisasi.urls')),
    #url(r'^organisasi/$', organisasiViews.index),
    url(r'^about/', include('about.urls')),
    url(r'^chat/', include('chat.urls')),
    url(r'^newsfeed/', include('newsfeed.urls')),
    url(r'^admin/', admin.site.urls)
    
]