from django import forms
from .models import Trading

class BidForm(forms.ModelForm):
	class Meta:
		model 		= Trading
		fields 		= ['your_bid_price']