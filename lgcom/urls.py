from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^index/$', views.index,name='index'),
    url(r'^about/$', views.about,name='about'),
    url(r'^ip_list/$', views.ip_list, name='ip_list'),

   
]