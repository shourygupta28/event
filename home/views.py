from django.shortcuts import render

def home(request):
	return render(request, 'home/index.html', )

def trading(request):
	return render(request, 'home/trading.html')

def bidding(request):
	return render(request, 'home/letsbid.html')

def mycompanies(request):
	return render(request, 'home/mycompanies.html')

