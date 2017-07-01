from django.db import models



# Create your models here.
class IPAddress(models.Model):
	ip_address = models.GenericIPAddressField(max_length=50)
	ip_status = models.BooleanField(default=False)


	def __str__(self):
		return self.ip_address

	def change_status(self):
		if self.ip_status == True:
			self.ip_status = False
		else:
			self.ip_status = True
