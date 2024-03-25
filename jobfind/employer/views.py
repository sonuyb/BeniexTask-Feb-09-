from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from.forms import *
from . models import *

@login_required
def employeedash(request):
    return render(request,'employer/empdashboard.html')

@login_required
def createjob(request):
    jobform = JobForm()
    if request.method == 'POST':
        jobform = JobForm(request.POST)
        if jobform.is_valid():
            job = jobform.save(commit=False)
            job.user = request.user
            job.save()
            return display_job(request)
    else:
        jobform = JobForm()
    return render(request,'employer/createjob.html',{'jobform':jobform})

@login_required
def display_job(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request,'jobs/job_listing.html',{'jobs':jobs})

@login_required
def edit(request,pk):
    instance_edit = Job.objects.get(pk=pk)
    if request.POST:
        jobform = JobForm(request.POST, instance=instance_edit)
        if jobform.is_valid():
            instance_edit.save()
            return display_job(request)
    else:
        jobform = JobForm(instance=instance_edit)
    return render(request,'employer/createjob.html',{'jobform':jobform})

@login_required
def delete(request,pk):
    instance = Job.objects.get(pk=pk)
    instance.delete()
    # jobs = Job.objects.all()
    return display_job(request)
    # return redirect('delete')

@login_required
def view_applicants(request,job_id):
    job = get_object_or_404(Job, pk=job_id)
    applicants = JobApplicant.objects.filter(job=job)
    return render(request,'employer/viewapplicants.html', {'applicants': applicants, 'job': job})

@login_required
def emp_logout(request):
    logout(request)
    return render(request,'login.html')