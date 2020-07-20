from django.db import models

class User(models.Model):
	Name = models.CharField(max_length=50)
	Contact = PhoneNumberField(blank=False, null=False, help_text='Add country code before the contact no.')
	ECoins = models.IntergerField()

	def __str__(self):
		return self.title