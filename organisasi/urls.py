from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^members/$', views.members),
    url(r'^dokumen/$', views.dokumen),
    url(r'^$', views.index),

]