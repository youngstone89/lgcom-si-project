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
			email=self.normalize_email(self.email),
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
			email=self.normalize_email(self.email),
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
	REQUIRED_FIELDS = [] 

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


class IPAddress(models.Model):
	ip_address = models.GenericIPAddressField(max_length=50, primary_key=True, unique=True)
	ip_status = models.BooleanField(default=False)
	ipuser = models.ForeignKey(MyUser,on_delete=models.CASCADE, null=True, blank=True,to_field='email')


	def __str__(self):
	 	return self.ip_address
	# 	return "{0},{1}".format(self.ip_address,self.ip_status)


class Project(models.Model):
	team = models.CharField(max_length=20, default='마케팅플랫폼팀')
	sm_si_choices = (('si','si'),('sm','sm'),)
	project_code = models.CharField(max_length=20, primary_key=True, unique=True)
	project_name = models.CharField(max_length=50, unique=True)
	project_manager = models.CharField(max_length=20)
	sm_si = models.CharField(max_length=10, choices=sm_si_choices)

	def __str__(self):
		return self.project_name
	# def __str__(self):
	# 	return "{0},{1},{2},{3},{4},{5},{6}".format(self.team,self.project_code,self.project_name,self.project_manager,self.sm_si)

	
class Contract(models.Model):

	contract_code = models.CharField(max_length=20,primary_key=True, unique=True)
	contract_name = models.CharField(max_length=20, unique=True)
	project = models.ForeignKey(Project,on_delete=models.CASCADE,to_field='project_name')

	def __str__(self):
		return self.contract_name
	# 	return "{0},{1}".format(self.contract_code,self.contract_name)

class ContractMember(models.Model):

	company_choices=(('비비엠씨(주)','비비엠씨(주)'),('(주)지엠솔루션','(주)지엠솔루션'),('(주)더피프티원','(주)더피프티원'),('(주)비즈테크파트너스','(주)비즈테크파트너스'),)
	company = models.CharField(max_length=20,choices=company_choices)
	member_name = models.CharField(max_length=20)
	period = models.CharField(max_length=50)
	man_month = models.DecimalField(default=0.0, decimal_places=2,max_digits=4)
	contract_level = models.CharField(max_length=30)
	contract = models.ForeignKey(Contract,on_delete=models.CASCADE,to_field='contract_name')

	def __str__(self):
		return self.member_name
	# 	return "{0},{1},{2},{3},{4}".format(self.company,self.member_name,self.period,self.man_month,self.contract_level)

class Officeplus(ContractMember):


	external_email= models.OneToOneField(MyUser,to_field='email', unique=True, primary_key=True)
	position = models.CharField(max_length=10)
	lastname = models.CharField(max_length=10)
	firstname = models.CharField(max_length=10)
	project = models.ForeignKey(Project,on_delete=models.CASCADE,to_field='project_name')


	
	# 	return "{0},{1},{2},{3},{4},{5},{6},{7},{8}".format(
	# 		super(self).company,
	# 		super(self).member_name,
	# 		super(self).period, 
	# 		super(self).man_month,
	# 		super(self).contract_level,
	# 		self.external_email,
	# 		self.position,
	# 		self.lastname,
	# 		self.firstname,
		
	# 		)
	
