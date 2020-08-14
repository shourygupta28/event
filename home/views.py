from django.shortcuts import render, redirect
from .models import Company, Trading, Share, Bidding
from users.models import User
from .forms import TradeForm, BidForm

def coming(request):
	return render(request, 'home/comingsoon.html')


def home(request):
	context = {
		'Companys': Company.objects.all()
	}
	return render(request, 'home/index.html', context)



##############################################
# trading view not required, can be deleted
##############################################

# def trading(request, id=None):
# 	if request.method == 'POST':
# 		form = TradeForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			# messages.success(request, f'Your account has been created! You can login now.')
# 			return redirect('trading')

# 	else:
# 		form = TradeForm()

# 	context = {
# 		'form':form,
# 		'Tradings': Trading.objects.all(),
# 		'Companys': Company.objects.all(),
# 	}
	
# 	# print(context[trading])
# 	return render(request, 'home/trading.html', context)


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

def mycompanies(request):
	context = {
		'Shares': Share.objects.all(),
	}
	return render(request, 'home/mycompanies.html', context)

