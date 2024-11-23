from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Application
from .forms import JobForm, ApplicationForm
from django.contrib import messages

# Home Page - List Jobs
def home(request):
    jobs = Job.objects.all().order_by('-posting_date')
    return render(request, 'jobs/home.html', {'jobs': jobs})

# Job Details and Application
def job_details(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(request, "Application submitted successfully!")
            return redirect('home')
    else:
        form = ApplicationForm()
    return render(request, 'jobs/job_details.html', {'job': job, 'form': form})

# Admin - Add New Job
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job posted successfully!")
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})

# Admin - View Applications
def view_applications(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    applications = Application.objects.filter(job=job)
    return render(request, 'jobs/view_applications.html', {'job': job, 'applications': applications})
