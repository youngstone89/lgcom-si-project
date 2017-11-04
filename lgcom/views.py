from django.shortcuts import render
from django.http import HttpResponse
# from .models import IPAddress
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .forms import (UserCreationForm, UserChangeForm)
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):

	return render(request, 'lgcom/index.html')


def get_start(request):

	return render(request, 'lgcom/getting_started.html')



def ip_list(request):
	
	iplist = IPAddress.objects.all()

	if iplist:
		return render(request, 'lgcom/ip_list.html', {'iplist':iplist})
	else:
		return render(request, 'lgcom/error.html', {})


class CreateUserView(CreateView):
	template_name = 'registration/signup.html'
	form_class = UserCreationForm # class to instantiate
	success_url = 'create_user_done'  #The URL to redirect to when the form is successfully processed.

class RegisteredView(TemplateView):
	template_name = 'registration/signup_done.html'
