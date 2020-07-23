from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	email 				= models.EmailField(verbose_name='Email Address', unique=True)
	name				= models.CharField(max_length=50)
	contact_no			= PhoneNumberField(blank=False, null=False, help_text='Add country code before the contact no.')
	eCoins				= models.DecimalField(decimal_places=2, max_digits= 9, default=00)
	# Companies


	USERNAME_FIELD 		= 'email'
	user_permissions 	= None
	groups				= None
	REQUIRED_FIELDS = ['email','name','contact_no']
	def __str__(self):
		return self.title