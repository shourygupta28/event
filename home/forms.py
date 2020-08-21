from django import forms
from .models import Trading, Bidding
from django.core.validators import MaxValueValidator, MinValueValidator


class TradeForm(forms.ModelForm):
	class Meta:
		model 		= Trading
		fields 		= ['highest_bid']

class BidForm(forms.ModelForm):
	class Meta:
		model 		= Bidding
		fields 		= ['bidding_price']

class CompanyForm(forms.ModelForm):
	lowest_bid_price = forms.IntegerField(validators=[MinValueValidator(0)])
	class Meta:
		model 		= Trading
		fields 		= ['percentage_for_sale', 'lowest_bid_price']