from django.db import models

class Entry(models.Model):
	first_name = models.CharField(max_length = 25)
	last_name = models.CharField(max_length = 25)
	street_address = models.CharField(max_length = 150)
	email = models.EmailField(max_length = 254, unique=True)
	phone_number = models.CharField(max_length = 14, unique=True)

	def __unicode__(self):
		return self.email

#Add vendor customer field
#Add date added field