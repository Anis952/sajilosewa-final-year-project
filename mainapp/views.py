from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required()
def customer(request):
    return render(request, 'customer.html')   

@login_required()
def courier(request):
    return render(request, 'courier.html') 

# def sign_in(request):
#     return render(request, 'sign-in.html') 

def sign_up(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email').lower()

            user = form.save(commit=False)
            user.username = email
            user.save()

            #send welcome email

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')



    return render(request, 'sign_up.html',
    {'form':form})