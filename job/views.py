from django.shortcuts import render
from .models import Job

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    context ={'Job' : job_list}
    return render(request,'Job/job_list.html', context=context)
     

def job_detail(request, id):
    job_detail = Job.objects.get(id = id)
    context ={'Job' : job_detail}
    return render(request, 'Job/job_detail.html',context=context)