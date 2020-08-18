from django.shortcuts import render, redirect
from .models import Company, Trading, Share, Bidding
from users.models import User
from .forms import TradeForm, BidForm, CompanyForm

def coming(request):
	return render(request, 'home/comingsoon.html')


def home(request):
	context = {
		'Companys': Company.objects.all()
	}
	return render(request, 'home/index.html', context)


def tradingUpdateView(request, id=None):
	if id:
		trade = Trading.objects.get(id = id)
		if request.method == 'POST':
			form = TradeForm(request.POST, instance=trade)
			if form.is_valid():
				form.save()
			return redirect('trading')
	else:
		form = TradeForm()

	context = {
		'form':form	,
		'Tradings': Trading.objects.all(),
		'Companys': Company.objects.all(),
	}

	return render(request, 'home/trading.html', context)
	


def bidding(request, id=None):
	if id:
		bid = Bidding.objects.get(id = id)
		if request.method == 'POST':
			form = BidForm(request.POST, instance=bid)
			if form.is_valid():
				form.save()
			return redirect('bidding')
	else:
		form = BidForm()
	context = {
		'form' : form,
		'Bid': Bidding.objects.all(),
		'Companys': Company.objects.all()	
	}
	return render(request, 'home/letsbid.html', context)


def mycompanies(request, id=None):
	if id:
		current_share = Share.objects.get(id = id)
		if request.method == 'POST':
			form = CompanyForm(request.POST)
			if form.is_valid():
				form.instance.company = current_share.company
				form.save()
			return redirect('trading')
	else:
		form = CompanyForm()

	context = {
		'form' : form,
		'Shares': Share.objects.filter(shareholder=request.user),
	}
	return render(request, 'home/mycompanies.html', context)

def newpage(request):
    return render(request, 'home/newpage.html')

