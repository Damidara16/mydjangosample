from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .forms import contactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    title = "My Life"
    return render(request, 'proj_1/client.html', {"title": title})

def success(request):
    return render(request, 'proj_1/success.html')

def home(request):
    title = "test code"
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            fName = form.cleaned_data['fName']
            lName = form.cleaned_data['lName']

            try:
                send_mail(email, fName, lName, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    else:
        form = contactForm()
        context = {"title":title, "form":form}
    return render(request, 'proj_1/home.html', context)
