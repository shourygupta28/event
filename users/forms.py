from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Users
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from .models import Users

class UserRegistrationForm(UserCreationForm):