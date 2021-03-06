from audioop import reverse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from grpc import Status
import requests

from mainapp.models import *


# Create your views here.
@login_required(login_url="/sign-in/?next=/courier/")
def home(request):
    return redirect(reverse('courier:available_jobs'))

 

@login_required(login_url="/sign-in/?next=/courier/")
def available_jobs_page(request):
  
     return render(request, 'courier/available_jobs.html', {
        "GOOGLE_MAP_API_KEY": settings.GOOGLE_MAP_API_KEY
    })


@login_required(login_url="/sign-in/?next=/courier/")
def available_job_page(request, id):
    job = Job.objects.filter(id=id, status=Job.PROCESSING_STATUS).last()

    if not job:
        return redirect(reverse('courier:available_jobs'))
    
    if request.method == 'POST':
        job.courier = request.user.courier
        job.status = Job.PICKING_STATUS
        job.save()

        return redirect(reverse('courier:available_jobs'))

    return render(request, 'courier/available_job.html',{
        "job": job,
        
    })

@login_required(login_url="/sign-in/?next=/courier/")
def current_job_page(request):
    job = Job.objects.filter(
        courier=request.user.courier,
        status__in = [
            Job.PICKING_STATUS,
            Job.DELIVERING_STATUS
        ]
    ).last()

    return render(request, 'courier/current_job.html', {
        "job": job,
        "GOOGLE_MAP_API_KEY": settings.GOOGLE_MAP_API_KEY
    })

@login_required(login_url="/sign-in/?next=/courier/")
def current_job_take_photo_page(request, id):
    job = Job.objects.filter(
        id=id,
        courier=request.user.courier,
        status__in=[
            Job.PICKING_STATUS,
            Job.DELIVERING_STATUS
        ]
    ).last()

    if not job:
        return redirect(reverse('courier:current_job'))

    return render(request, 'courier/current_job_take_photo.html', {
        "job": job
    })
@login_required(login_url="/sign-in/?next=/courier/")
def job_complete_page(request):
    return render (request, 'courier/job_complete.html')

@login_required(login_url="/sign-in/?next=/courier/")
def archived_jobs_page(request):
    jobs = Job.objects.filter(
        courier=request.user.courier,
        status=Job.COMPLETED_STATUS
    )

    return render(request, 'courier/archived_jobs.html', {
        "jobs": jobs
    })
