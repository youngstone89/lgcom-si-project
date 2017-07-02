from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^index/$', views.index,name='index'),
    url(r'^about/$', views.about,name='about'),
    url(r'^ip_list/$', views.ip_list, name='ip_list'),
    url(r'^accounts/signup$', views.CreateUserView.as_view(), name='signup'),
    url(r'^accounts/create_user_done$', views.RegisteredView.as_view(), name='create_user_done'),
    url(r'^accounts/login/$',auth_views.login, name='login',kwargs={'template_name':'authentication/login.html'}),
    url(r'^accounts/logout/$',auth_views.logout, name='logout',kwargs={'next_page':settings.LOGIN_URL}),

   
]