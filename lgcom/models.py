from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.


class MyUserManager(BaseUserManager):
	def create_user(self,email,username,password):
		if not email:
			raise ValueError("이메일을 입력하시오")

		if not username:
			raise ValueError("성명을 입력하시오")

		if not password:
			raise ValueError("비밀번호를 입력하시오")

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			password=password,)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,username,password):
		if not email:
			raise ValueError("이메일을 입력하시오")

		if not username:
			raise ValueError("성명을 입력하시오")

		if not password:
			raise ValueError("비밀번호를 입력하시오")
		user = self.model(
			email=self.normalize_email(email),
			username=username,
			password=password,)
		user.is_admin = True
		user.save(using=self._db)
		return user

class MyUser(AbstractBaseUser):

	SI = 'SI'
	SM = 'SM'

	USER_GROUP_CHOICES = ((SI,SI),(SM,SM),)

	
	HUMAN = 'HUMAN'
	DEVICE = 'DEVICE'

	USER_TYPE_CHOICES = ((HUMAN,HUMAN),(DEVICE,DEVICE),)

	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
		primary_key=True,
		)
	username = models.CharField(
		verbose_name='성명',
		max_length=30,
		unique=False,
		primary_key=False,
		help_text='한글이름',
		)
	user_company = models.CharField(max_length=20)
	user_type = models.CharField(max_length=5,choices=USER_TYPE_CHOICES,default=HUMAN)
	user_group = models.CharField(max_length=2,choices=USER_GROUP_CHOICES,default=SI)
	is_partner = models.BooleanField(default=False)

	
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD ='email'
	REQUIRED_FIELDS = ['username'] 

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.email 

	def get_short_name(self):
		return self.email  

	def __str__(self):
		return self.email 

	def has_perm(self,perm,obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True 

	def has_module_perms(self,app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True 

	def is_staff(self):
		return self.is_admin



class PartnerResourceState(models.Model):
	team = models.CharField(max_length=50, default="마케팅플랫폼팀")
	pjt_code = models.CharField(max_length=100)
	pjt_name = models.CharField(max_length=100)
	crt_code = models.CharField(max_length=100)
	crt_name = models.CharField(max_length=100)
	pm_name = models.CharField(max_length=100)
	sm_si = models.CharField(max_length=100)
	ptr_cpny = models.CharField(max_length=100)
	kor_name = models.CharField(max_length=100)
	crt_period = models.CharField(max_length=100)
	man_month = models.DecimalField(decimal_places=1,max_digits=3)
	level = models.CharField(max_length=100)
	price = models.PositiveIntegerField(default=0.0)
		
	

	def __str__(self):
		return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},".format(self.team,self.pjt_code,self.pjt_name,self.crt_code, self.crt_name,self.pm_name,self.sm_si,self.ptr_cpny,self.kor_name,self.crt_period,self.man_month,self.level,self.price)


class Project(models.Model):
	pjt_code = models.CharField(max_length=100, primary_key=True)
	pjt_name = models.CharField(max_length=100)

	def __str__(self):
		return "{0}{1}{2}".format(self.pjt_code,"-",self.pjt_name)

class Contract(models.Model):
	crt_code = models.CharField(max_length=100, primary_key=True)
	crt_name = models.CharField(max_length=100)
	project = models.ForeignKey(Project,to_field='pjt_code', null=True)


	def __str__(self):
		return "{0}{1}".format(self.crt_code,self.crt_name)

class ContractMember(models.Model):

	kor_name_crt_period_level = models.CharField(max_length=200, primary_key=True)
	ptr_cpny = models.CharField(max_length=100)
	man_month = models.DecimalField(decimal_places=1,max_digits=3)
	price = models.PositiveIntegerField(default=0.0)
	contract=models.ForeignKey(Contract,to_field='crt_code', null=True)

	def __str__(self):
		return "{0}".format(self.kor_name_crt_period_level)

class IPAddress(models.Model):

	ipaddress = models.GenericIPAddressField(primary_key=True,protocol='IPv4')
	occupant = models.ForeignKey(MyUser,to_field='email', related_name='occupants',null=True)
	def __str__(self):
		return "{0}".format(self.ipaddress)