from django.shortcuts import render
from .models import Job

# when user selects home following function is executed 
#passes the html and jobs model object
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})