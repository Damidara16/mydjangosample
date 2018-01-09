from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def index(request):
    return render(request, 'proj_1/home.html')

class homeView(TemplateView):

    template_name = "proj_1/index.html"
