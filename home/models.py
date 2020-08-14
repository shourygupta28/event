from django.db import models
from users.models import User

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=30)
    multiplication_factor = models.PositiveIntegerField()
    

    def __str__(self):
        return self.company_name

class Trading(models.Model):
    company = models.ForeignKey(Company, related_name = 'company_details_trading', on_delete=models.CASCADE, null=True, blank=True)
    your_bid_price = models.IntegerField(default=0)
    highest_bid = models.IntegerField(default=0)
    # user = models.ForeignKey(User,on_delete)
    # percentage_for_sale = models.IntegerField(blank=True)

class Share(models.Model):
    company = models.ManyToManyField(Company, related_name = 'company_details')
    shareholder = models.ManyToManyField(User, related_name = 'shareholder_details')
    percentage_of_share = models.IntegerField() 

class Bidding(models.Model):
    company = models.ForeignKey(Company, related_name = 'company_details_bidding', on_delete=models.CASCADE)
    bidding_price = models.IntegerField()