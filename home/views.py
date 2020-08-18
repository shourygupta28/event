from django.shortcuts import render, redirect
from .models import Company, Trading, Bidding
from users.models import User
from .forms import TradeForm, BidForm, CompanyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Share as var


def coming(request):
	return render(request, 'home/comingsoon.html')

def comingbidding(request):
	return render(request, 'home/comingsoon.html')

def home(request):
	context = {
		'Companys': Company.objects.all()
	}
	return render(request, 'home/index.html', context)

def timepage(request):
	return render(request, 'home/save.html')

def time(request):

	i = var.objects.all();
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print(i)
	for j in i:
		print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		print(j)
		coin = j.shareholder.eCoins + j.percentage_of_share*j.company.multiplication_factor*10
		j.save()
		print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		print(coin)
		print(j.shareholder.contact_no)
		print(j.shareholder.name)
		User.objects.filter(id = j.shareholder.id).update(eCoins = coin)

	# context = {
	# 	'Shares': Share.objects.all()
	# }
	return redirect('timepage')

@login_required()
def tradingUpdateView(request, id=None):
	if id:
		trade = Trading.objects.get(id = id)
		if request.method == 'POST':
			form = TradeForm(request.POST, instance=trade)
			if trade.highest_bid < int(form['highest_bid'].value()) and form.is_valid():
				trade.buyer = request.user
				form.save()
			else:
				messages.add_message(request, messages.INFO, 'Enter a Bid Price higher than the current Highest Bid Price')
			return redirect('trading')
	else:
		form = TradeForm()

	context = {
		'form':form	,
		'Tradings': Trading.objects.all(),
		'Companys': Company.objects.all(),
	}

	return render(request, 'home/trading.html', context)
	

@login_required()
def bidding(request, id=None):
	if id:
		bid = Bidding.objects.filter(id = id).first()
		if request.method == 'POST':
			form = BidForm(request.POST, instance=bid)
			if bid.bidding_price < int(form['bidding_price'].value()) and form.is_valid():
				bid.buyer = request.user
				form.save()
			else:
				messages.add_message(request, messages.INFO, 'Enter a Bid Price higher than the current Highest Bid Price')
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

