from django.http import HttpResponse
from django.shortcuts import render
from portfolio_app.models import Project


# Create your views here.
# def project_view(request):
#     return HttpResponse("cia tavo atzduojamas http")

def home_view(request):
    return render(request, 'home.html')

def project_view(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})

def contacts_view(request):
    return render(request, 'contacts.html')

