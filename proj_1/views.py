from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def index(request):
    title = "My Life"
    return render(request, 'proj_1/client.html', {"title": title})

def home(request):
    title = "test code"
    return render(request, 'proj_1/home.html', {"title": title})
