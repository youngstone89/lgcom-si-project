from django.shortcuts import render
from django.http import HttpResponse
from .models import IPAddress
# Create your views here.

def index(request):

	return render(request, 'lgcom/index.html')


def about(request):

	return render(request, 'lgcom/getting_started.html')



def ip_list(request):
	
	iplist = IPAddress.objects.all()

	if iplist:
		return render(request, 'lgcom/ip_list.html', {'iplist':iplist})
	else:
		return render(request, 'blog/error.html', {})