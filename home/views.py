from django.shortcuts import render, redirect
from .models import Company, Trading
from users.models import User
from .forms import TradeForm, BidForm, CompanyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Share as var
from .models import  Bidding as bidvar
from django.core.paginator import Paginator
import time as setInterval
from django.views.defaults import page_not_found, server_error
# from threading import Timer

def trade(request):
	return render(request, 'home/trade-close.html')


def alert_update(request):
	User.objects.filter(id=request.user.id).update(alert='')
	return redirect('mycompanies')


def add_mycompanies(request):
	if request.user.is_superuser:
		for bid in bidvar.objects.all():
			if bid.buyer:
				temp = var.objects.filter(company=bid.company)
				if not temp:
					var.objects.create(company=bid.company,
								  	   shareholder=bid.buyer,
								   	   percentage_of_share=100)
					coins = User.objects.get(id=bid.buyer.id).eCoins - bid.bidding_price
					print(coins)
					User.objects.filter(id=bid.buyer.id).update(eCoins=coins)
		return redirect('timepage')
	else:
		return redirect('home')
	

def coming(request):
	return render(request, 'home/comingsoon.html')

def closed(request):
    return render(request, 'home/closed.html')

def trading_closed(request):
	return render(request, 'home/closed_trading.html')


def comingbidding(request):
	return render(request, 'home/comingsoon.html')

def company(request, pg=1):
	company_list = Company.objects.order_by('id')
	paginator = Paginator(company_list, 25)

	context = {
		'Companys' : paginator.page(pg),
		'page' : pg,
		'paginator' : paginator,
	}
	return render(request, 'home/companies.html', context)


def timepage(request):
	if request.user.is_superuser:
		return render(request, 'home/save.html')
	else:
		return redirect('comingsoon')


def time(request):
	if request.user.is_superuser:
		i = var.objects.all();
		for j in i:
			coin = j.shareholder.eCoins + j.percentage_of_share*j.company.multiplication_factor*10
			User.objects.filter(id = j.shareholder.id).update(eCoins = coin)
		return redirect('timepage')
	else:
		return redirect('comingsoon')


@login_required()
def tradingUpdateView(request, id=None, pg=1):
	if id:
		if not Trading.objects.filter(id = id):
			return render(request, 'home/trade-close.html')
		trade = Trading.objects.get(id = id)
		if request.method == 'POST' and trade.seller != request.user:
			form = TradeForm(request.POST, instance=trade)
			if trade.highest_bid < int(form['highest_bid'].value()):
				prev_bid = trade.highest_bid
				if request.user.eCoins >= int(form['highest_bid'].value()):
					if int(form['highest_bid'].value())%100 == 0 and form.is_valid():
						if trade.buyer != trade.seller:
							if trade.buyer != request.user:
								coins = User.objects.get(id=trade.buyer.id).eCoins + prev_bid
								User.objects.filter(id=trade.buyer.id).update(eCoins=coins)
							else:
								messages.add_message(request, messages.INFO, f'You are already the highest bidder on same company.' )
					else:
						messages.add_message(request, messages.INFO, f'You need to place bid in multiple of 100\'s only.' )
					trade.buyer = request.user
					form.save()
					coins = User.objects.get(id=trade.buyer.id).eCoins - trade.highest_bid
					User.objects.filter(id=trade.buyer.id).update(eCoins=coins)
					messages.add_message(request, messages.INFO, f'Your Bid has been placed sucessfully on {trade.company.company_name}.' )
				else:
					messages.add_message(request, messages.INFO, 'You don\'t have enough E-Coins to place this bid.' )
			else:
				messages.add_message(request, messages.INFO, 'Enter a bid price higher than the current highest bid price.')
		else:
			messages.add_message(request, messages.INFO, 'You can\'t bid on your own company')
		return redirect('trading', pg=pg)
	
	form = TradeForm()
	trade_list = Trading.objects.order_by('-id')
	paginator = Paginator(trade_list, 10)
	context = {
		'form':form,
		'Tradings' : paginator.page(pg),
		'page' : pg,
		'paginator' : paginator,
		'Companys': Company.objects.order_by('-id')
	}

	return render(request, 'home/trading.html', context)
	

@login_required
def tradingCloseView(request, id=None):
	trade = Trading.objects.get(id=id)
	if trade.seller == request.user:
		if trade.buyer != trade.seller:
			coins = request.user.eCoins + trade.highest_bid
			User.objects.filter(id=trade.seller.id).update(eCoins=coins)
		
			messages.add_message(request, messages.INFO, f'Trade has been closed successfully for {trade.highest_bid} E-Coins')
			
			alert_message = f'{trade.percentage_for_sale}% shares of the company \'{trade.company}\' have been added to your companies.'
			User.objects.filter(id=trade.buyer.id).update(alert=alert_message)
		
		obj = var.objects.filter(company=trade.company).filter(shareholder=trade.buyer)
		if obj:
			sum = obj.first().percentage_of_share + trade.percentage_for_sale
			obj.update(percentage_of_share=sum)
		else:
			var.objects.create(company=trade.company,
								 shareholder=trade.buyer,
								 percentage_of_share=trade.percentage_for_sale)
		trade.delete()
	return redirect('mytrade')

@login_required
def bidding(request, id=None, pg=1):
	if id:
		a = bidvar.objects.all();
		bid = bidvar.objects.filter(id = id).first()
		if request.method == 'POST':
			form = BidForm(request.POST, instance=bid)
			for b in a:
				if b.buyer == request.user:
					messages.add_message(request, messages.INFO, 'You can\'t have highest bid on two Companies')
					return redirect('bidding', pg=pg)						
			if bid.bidding_price < int(form['bidding_price'].value()):
				if request.user.eCoins > int(form['bidding_price'].value()):
					if int(form['bidding_price'].value())%100 == 0 and form.is_valid():
						bid.buyer = request.user
						form.save()	
						messages.add_message(request, messages.INFO, f'Your Bid has been placed sucessfully on {bid.company.company_name}' )
					else:
						messages.add_message(request, messages.INFO, 'You need to place bid in multiple of 100\'s only.'  )				

				else:
					messages.add_message(request, messages.INFO, 'You don\'t have enough E-Coins to place this bid.' )				
			else:
				messages.add_message(request, messages.INFO, 'Enter a Bid Price higher than the current Highest Bid Price')
			return redirect('bidding', pg=pg)
	
	form = BidForm()
	bid_list = bidvar.objects.filter(visible=True).order_by('-id')
	paginator = Paginator(bid_list, 13)
	context = {
		'form' : form,
		'Bid' : paginator.page(pg),
		'page' : pg,
		'paginator' : paginator,
		'Companys': Company.objects.order_by('-id')	
	}
	return render(request, 'home/letsbid.html', context)


@login_required
def mycompanies(request, id=None):
	if id:
		current_share = var.objects.get(id = id)
		if request.method == 'POST':
			form = CompanyForm(request.POST)
			per_for_sale = int(form['percentage_for_sale'].value()) 
			if per_for_sale >= 5 and per_for_sale <= int(current_share.percentage_of_share) and form.is_valid():
				form.instance.company = current_share.company
				form.instance.your_bid_price = int(form['lowest_bid_price'].value())
				form.instance.seller = request.user
				form.instance.buyer = request.user
				obj = form.save()
				obj.highest_bid = form.cleaned_data.get('lowest_bid_price')
				obj.save()
				per_of_share = current_share.percentage_of_share - per_for_sale
				var.objects.filter(id=id).update(percentage_of_share=per_of_share)
				return redirect('trading', pg=1)
			elif per_for_sale < 5:
				messages.add_message(request, messages.INFO, 'You need to sell minimum 5 percent of Shares')
			elif per_for_sale > int(current_share.percentage_of_share):
				messages.add_message(request, messages.INFO, 'Add a value less than current share')
			return redirect('mycompanies')
	else:
		form = CompanyForm()

	context = {
		'form' : form,
		'Shares': var.objects.filter(shareholder=request.user).exclude(percentage_of_share=0).order_by('-id'),
	}
	return render(request, 'home/mycompanies.html', context)

def home(request):
    return render(request, 'home/home.html')


def mytrade(request):
	context = {
		'Trades': Trading.objects.filter(seller=request.user).order_by('-id'),
	}
	return render(request, 'home/mytrade.html', context)


def mybid(request):
	context = {
		'Trades': Trading.objects.filter(buyer=request.user).order_by('-id'),
	}
	return render(request, 'home/mybids.html', context)


def mycompanies_notrade(request):
	messages.add_message(request, messages.INFO, 'The trade can not be placed before 23-08-2020 17:00.')
	return redirect(mycompanies)

