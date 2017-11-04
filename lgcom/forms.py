from django.forms import ModelForm
# from .models import IPAddress
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import MyUser 
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField 

class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

	class Meta:
		model = MyUser
		fields = ('email', 'username','password1', 'password2')

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2 

	def save(self, commit=True): 
		user = super(UserCreationForm,self).save(commit=False) 
		user.email = self.cleaned_data["email"]
		user.username = self.cleaned_data["username"]
		user.set_password(self.cleaned_data['password1'])

		if commit:
			user.save()
		return user 

class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = MyUser 
		fields = ('email','username','password')


	def clean_password(self):
		return self.initial["password"]
