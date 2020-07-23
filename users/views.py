from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user                = form.save()
            student.name        = form.cleaned_data.get('name')

    else:
        form = UserRegistrationForm()
    return render(request, 'users/signup.html', {'form': form})