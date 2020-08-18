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
    buyer = models.OneToOneField(User, related_name = 'trading_buyer', on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(User, related_name = 'trading_seller', on_delete=models.CASCADE,  null=True, blank=True)
    percentage_for_sale = models.DecimalField(default=1.00, decimal_places = 2, max_digits = 3 )
    # user = models.ForeignKey(User,on_delete)
    # percentage_for_sale = models.IntegerField(blank=True)
    
class Share(models.Model):
    company = models.ForeignKey(Company, default=None, on_delete=models.CASCADE ,related_name = 'company_details')
    shareholder = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name = 'shareholder_details')
    percentage_of_share = models.IntegerField() 

class Bidding(models.Model):
    company = models.ForeignKey(Company, related_name = 'company_details_bidding', on_delete=models.CASCADE)
    bidding_price = models.IntegerField()
    buyer = models.OneToOneField(User, related_name = 'bidding_buyer', on_delete=models.CASCADE, null=True, blank=True)