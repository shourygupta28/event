from django.shortcuts import render, redirect
from .models import Company, Trading, Share, Bidding
from users.models import User
from .forms import BidForm


def home(request):
	context = {
		'Companys': Company.objects.all()
	}
	return render(request, 'home/index.html', context)


def trading(request, id=None):
	if request.method == 'POST':
		form = BidForm(request.POST)
		if form.is_valid():
			Trading = form.save()

			# messages.success(request, f'Your account has been created! You can login now.')
			return redirect('trading')

	else:
	form = BidForm()

	context = {
		'form':form,
		'Tradings': Trading.objects.all(),
		'Companys': Company.objects.all(),
	}
	
	# print(context[trading])
	return render(request, 'home/trading.html', context)

def tradingUpdateView(request, id=None):
	trade = Trading.objects.get(id = id)
	if request.method == 'POST':
		form = BidForm(request.POST, instance=trade)
		if form.is_valid():
			form.save()
			return redirect('trading')
	else:
		form = BidForm(instance=trade)

	context = {
		'form':form	
	}

	return render(request, 'home/trading.html', context)
	


def bidding(request):
	context = {
		'Bid': Bidding.objects.all(),
		'Companys': Company.objects.all()	
	}
	return render(request, 'home/letsbid.html', context)

def mycompanies(request):
	context = {
		'Shares': Share.objects.all(),
	}
	return render(request, 'home/mycompanies.html', context)

