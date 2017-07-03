from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class IPAddress(models.Model):
	ip_address = models.GenericIPAddressField(max_length=50)
	ip_status = models.BooleanField(default=False)


	def __str__(self):
		return self.ip_address


class IPUser(User):
	
	SI = 'SI'
	SM = 'SM'

	USER_GROUP_CHOICES = ((SI,SI),(SM,SM),)

	USER_GROUP = models.CharField(max_length=2,choices=USER_GROUP_CHOICES,default=SI)

	HUMAN = 'HUMAN'
	DEVICE = 'DEVICE'

	USER_TYPE_CHOICES = ((HUMAN,HUMAN),(DEVICE,DEVICE),)
	USER_TYPE = models.CharField(max_length=5,choices=USER_TYPE_CHOICES,default=HUMAN)

	def __str__(self):
		return 'IP User Info: {0},{1},{2}'.format(self.username, self.USER_TYPE, self.USER_GROUP)