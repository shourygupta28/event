from django import forms
from .models import Trading, Bidding

class TradeForm(forms.ModelForm):
	class Meta:
		model 		= Trading
		fields 		= ['highest_bid']

class BidForm(forms.ModelForm):
	class Meta:
		model 		= Bidding
		fields 		= ['bidding_price']