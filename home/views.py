from django.shortcuts import render, redirect
from .models import Company, Trading
from users.models import User
from .forms import TradeForm, BidForm, CompanyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Share as var
from .models import  Bidding as bidvar


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
	# print(i)
	for j in i:
		coin = j.shareholder.eCoins + j.percentage_of_share*j.company.multiplication_factor*10
		User.objects.filter(id = j.shareholder.id).update(eCoins = coin)
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
		a = bidvar.objects.all();
		bid = bidvar.objects.filter(id = id).first()
		if request.method == 'POST':
			form = BidForm(request.POST, instance=bid)
			if bid.bidding_price < int(form['bidding_price'].value()) and form.is_valid():				
				for b in a:
					print("$$$$$$$$$$$$$$$$$$$")
					print(b)
					print("$$$$$$$$$$$$$$$$$$$")
					if b.shareholder == request.user:
						messages.add_message(request, messages.INFO, 'You cant have higest bid on two Companies')
					else:
						bid.buyer = request.user
						form.save()					
			else:
				messages.add_message(request, messages.INFO, 'Enter a Bid Price higher than the current Highest Bid Price')
			return redirect('bidding')
	else:
		form = BidForm()
	context = {
		'form' : form,
		'Bid': bidvar.objects.all(),
		'Companys': Company.objects.all()	
	}
	return render(request, 'home/letsbid.html', context)

def mycompanies(request, id=None):
	if id:
		current_share = var.objects.get(id = id)
		trade = Trading.objects.filter(id = id).first()
		if request.method == 'POST':
			form = CompanyForm(request.POST)
			if int(form['percentage_for_sale'].value()) > 5 and int(form['percentage_for_sale'].value()) < 49 and int(form['percentage_for_sale'].value()) < int(current_share.percentage_of_share) and form.is_valid():
				form.instance.company = current_share.company
				form.instance.your_bid_price = int(form['highest_bid'].value())
				form.instance.seller = request.user
				form.instance.buyer = request.user
				form.save()
			elif int(form['percentage_for_sale'].value()) < 5:
				messages.add_message(request, messages.INFO, 'You need to sell minimum 5 percent of Shares')
			elif int(form['percentage_for_sale'].value()) > int(current_share.percentage_of_share):
				messages.add_message(request, messages.INFO, 'Add a value less than current share')
			elif int(form['percentage_for_sale'].value()) > 49:
				messages.add_message(request, messages.INFO, 'Add a value more than 49%')
			return redirect('trading')
	else:
		form = CompanyForm()

	context = {
		'form' : form,
		'Shares': var.objects.filter(shareholder=request.user),
	}
	return render(request, 'home/mycompanies.html', context)

def newpage(request):
    return render(request, 'home/newpage.html')

def mytrade(request):
	context = {
		'Trades': Trading.objects.filter(seller=request.user),
	}
	return render(request, 'home/mytrade.html', context)
