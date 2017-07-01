from django.forms import ModelForm
from .models import IPAddress
from django.contrib.auth.models import User


class IPAaddressForm(ModelForm):
	class Meta:
		model = IPAddress


class UserForm(ModelForm):
	class Meta:
		model = User