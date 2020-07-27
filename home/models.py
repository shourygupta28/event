from django.db import models
from users.models import User

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=30)
    multiplication_factor = models.PositiveIntegerField()
    

    def __str__(self):
        return self.company_name

class Trading(models.Model):
    company_name = models.CharField(max_length=30, default= 'Company')
    multiplicationfactor = models.PositiveIntegerField(default=1)
    your_bid_price = models.IntegerField()
    percentage_for_sale = models.IntegerField()

