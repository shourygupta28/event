from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=30)
    multiplication_factor = models.DecimalField(default=1, decimal_places = 2, max_digits = 3)
    

    def __str__(self):
        return self.company_name

class Trading(models.Model):
    company = models.ForeignKey(Company, related_name = 'company_details_trading', on_delete=models.CASCADE, null=True, blank=True)
    your_bid_price = models.PositiveIntegerField(default=0)
    highest_bid = models.PositiveIntegerField(default=0)
    buyer = models.ForeignKey(User, related_name = 'trading_buyer', on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(User, related_name = 'trading_seller', on_delete=models.CASCADE,  null=True, blank=True)
    percentage_for_sale = models.DecimalField(default=1, decimal_places = 0, max_digits = 3 )
    
    def __str__(self):
        return self.company.company_name + " - " + str(self.percentage_for_sale) + " From " + str(self.seller) + " to " + str(self.buyer)

class Share(models.Model):
    company = models.ForeignKey(Company, default=None, on_delete=models.CASCADE ,related_name = 'company_details')
    shareholder = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name = 'shareholder_details')
    percentage_of_share = models.PositiveIntegerField(validators=[MaxValueValidator(100)]) 
    
    def __str__(self):
        return self.company.company_name + " - " + str(self.percentage_of_share) + " with " + str(self.shareholder)

class Bidding(models.Model):
    company = models.ForeignKey(Company, related_name = 'company_details_bidding', on_delete=models.CASCADE)
    bidding_price = models.PositiveIntegerField()
    buyer = models.ForeignKey(User, related_name = 'bidding_buyer', on_delete=models.CASCADE, null=True, blank=True)
    visible = models.BooleanField(default = False)

    def __str__(self):
        return self.company.company_name + " current " + str(self.buyer)