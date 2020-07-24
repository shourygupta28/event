from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from .models import User

class UserRegistrationForm(UserCreationForm):
	name 				= forms.CharField(max_length=60)
	Username 			= forms.CharField(max_length=15)
	email 				= forms.EmailField()

	class Meta(UserCreationForm.Meta):
		models 		= User
		fields 		= ['name','email','password1','password2']
	# name 				= forms.CharField(max_length=60)
	# email 				= forms.EmailField(help_text='Email Address')
	# # contact 			= PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('')}), label=("Phone number"), required=False, help_text='Add Country Code before your contact number.')
	
	# class Meta(UserCreationForm.Meta):
	# 	model 	= User
	# 	fields 	= ['name','email','password1','password2']
