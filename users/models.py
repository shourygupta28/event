from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
	# Username
	Name = models.CharField(max_length=50)
	# Password
	# E-Mail
	Contact = PhoneNumberField(blank=False, null=False, help_text='Add country code before the contact no.')
	ECoins = models.DecimalField(decimal_places=2, max_digits= 9)
	# Companies
	def __str__(self):
		return self.title