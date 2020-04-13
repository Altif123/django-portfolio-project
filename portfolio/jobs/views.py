from django.shortcuts import render, get_object_or_404
from .models import Job,Project

# when user selects home following function is executed 
#passes the html and jobs model object
def home(request):
    jobs = Job.objects
    projects = Project.objects
    return render(request, 'jobs/home.html', {'jobs':jobs, 'projects':projects })

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk = job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})