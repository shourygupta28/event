from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	"""docstring for User"""
	email 				= models.EmailField(verbose_name='Email Address', unique=True)
	name 				= models.CharField(max_length=50)
	eCoins 				= models.DecimalField(decimal_places=2, max_digits= 9, default=150000)
	contact_no 			= PhoneNumberField(blank=False, null=False, help_text='Add country code before the contact no.')

	USERNAME_FIELD 		= 'username'
	user_permissions 	= None
	groups 				= None
	REQUIRED_FIELDS 	= ['email']

	def __str__(self):
		return self.name
