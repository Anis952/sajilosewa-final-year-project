from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def home(request):
    return render(request, 'home.html')

 


# def courier(request):
#     return render(request, 'home.html') 