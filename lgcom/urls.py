from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

app_name = 'lgcom'

urlpatterns = [
	

	#/lgcom/
    url(r'^$',views.index, name='index'),
  
    #/lgcom/about
    url(r'^get_start/$', views.get_start,name='get_start'),

    #/lgcom/ip_list/
    url(r'^ip_list/$', views.ip_list, name='ip_list'),

    #/lgcom/accounts/signup/
    url(r'^accounts/signup/$', views.CreateUserView.as_view(), name='signup'),

    #/lgcom/accounts/create_user_done/
    url(r'^accounts/signup/create_user_done/$', views.RegisteredView.as_view(), name='create_user_done'),

    #/lgcom/accounts/login/
    url(r'^accounts/login/$',auth_views.login, name='login',kwargs={'template_name':'authentication/login.html'}),
   
   	#/lgcom/accounts/logout/
    url(r'^accounts/logout/$',auth_views.logout, name='logout',kwargs={'next_page':settings.LOGIN_URL}),

    #/lgcom/accounts/password_change
    url(r'^accounts/password_change/$', auth_views.PasswordChangeView.as_view(), name='password_change'),
   
   	#/lgcom/accounts/password_change/done/
    url(r'^accounts/password_change/done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    #/lgcom/accounts/password_reset/
    url(r'^accounts/password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),

    #/lgcom/accounts/password_reset/done
    url(r'^accounts/password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    #/lgcom/accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/
    url(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    #/lgcom/accounts/reset/done/
    url(r'^accounts/reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]