from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Job

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list,1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={'Jobs' : page_obj}
    return render(request,'Job/job_list.html', context=context)
     

def job_detail(request, slug):
    job_detail = Job.objects.get(slug = slug)
    context ={'Job' : job_detail}
    return render(request, 'Job/job_detail.html',context=context)