from django.shortcuts import render

def home(request):
	return render(request, 'home/base.html', )

# Create your views here.
