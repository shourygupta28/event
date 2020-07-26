from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User = form.save()

            messages.success(request, f'Your account has been created! You can login now.')
            return redirect('login')

    else:
        form = UserRegistrationForm()
    return render(request, 'users/signup.html', {'form': form})