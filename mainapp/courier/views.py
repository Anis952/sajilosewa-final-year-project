from audioop import reverse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings


# Create your views here.
@login_required(login_url="/sign-in/?next=/courier/")
def home(request):
    return redirect(reverse('courier:available_jobs'))

 

@login_required(login_url="/sign-in/?next=/courier/")
def available_job_page(request):
    return render(request, 'courier/available_jobs.html',{
        "GOOGLE_MAP_API_KEY":settings.GOOGLE_MAP_API_KEY
    }) 
