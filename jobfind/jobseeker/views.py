from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from employer.models import *
from . models import *
from.forms import *



def seekerdash(request):
    return render(request,'jobseeker/seekerdashboard.html')

@login_required
def registerjobseeker(request):
    registerform = JobSeekerRegister()
    if request.method == 'POST':
        registerform = JobSeekerRegister(request.POST,request.FILES)
        if registerform.is_valid():
            register = registerform.save(commit=False)
            register.user = request.user
            register.save()
            return redirect('profile')
    else:
        registerform = JobSeekerRegister()
    return render(request,'jobseeker/register.html',{'registerform':registerform})

@login_required
def jobseekerprofile(request):
    data = JobSeeker.objects.get(user=request.user)
    print(data.__dict__)
    return render(request,'jobseeker/profile.html',{'data':data})

@login_required
def editprofile(request,pk):
    instance = JobSeeker.objects.get(pk=pk)
    if request.POST:
        registerform = JobSeekerRegister(request.POST,instance=instance)
        if registerform.is_valid():
            instance.save()
            return jobseekerprofile(request)
    else:
        registerform = JobSeekerRegister(instance=instance)
    return render(request,'jobseeker/register.html',{'registerform':registerform})

@login_required
def display_all_job(request):
    query = request.GET.get('query')
    if query:
        jobs = Job.objects.filter(Q(is_available=True)& Q(job_title__icontains=query)|Q(state__icontains=query))
    else:
        jobs = Job.objects.filter(is_available=True)
    return render(request,'jobs/job_listing.html',{'jobs':jobs, 'user':request.user})

@login_required
def apply_job(request,pk):
    job = get_object_or_404(Job,pk=pk)
    if request.user.is_authenticated:
        job_seeker = JobSeeker.objects.get(user=request.user)
        job_application = JobApplicant.objects.get_or_create(job_seeker=job_seeker,job=job)
    return redirect('applied_job')

@login_required
def applied_jobs(request):
    jobs_obj = JobApplicant.objects.filter(job_seeker__user=request.user)
    print(jobs_obj)
    return render(request,'jobseeker/applied_jobs.html', {'jobs':jobs_obj})

@login_required
def seeker_logout(request):
    logout(request)
    return render(request,'login.html')