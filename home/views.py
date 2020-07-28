from django.shortcuts import render
from .models import Company, Trading

def home(request):
	context = {
		'Companys': Company.objects.all()
	}
	return render(request, 'home/index.html', context)

def trading(request):
	return render(request, 'home/trading.html')

def bidding(request):
	return render(request, 'home/letsbid.html')

def mycompanies(request):
	return render(request, 'home/mycompanies.html')

