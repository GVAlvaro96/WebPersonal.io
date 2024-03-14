from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    context ={'projects': projects}
    return render(request,"portfolio/portfolio.html", context)

def fcshot(request):
    return render(request, 'portfolio/fcshot.html')

def webpersonal(request):
    return render(request, 'portfolio/webpersonal.html')

def webempresarial(request):
    return render(request, 'portfolio/caffettiera.html')