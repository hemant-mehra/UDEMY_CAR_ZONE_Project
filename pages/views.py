from django.shortcuts import render
from django.http import HttpResponse
from pages import models
# Create your views here.


def home(request):
    teams = models.Team.objects.all()
    # team passed as context dictionary to home page
    return render(request, "pages/home.html", {"teams": teams})
    # return HttpResponse("hello world httpresponce")


def about(request):
    teams = models.Team.objects.all()
    return render(request, "pages/about.html", {"teams": teams})


def services(request):
    return render(request, "pages/services.html")


def contact(request):
    return render(request, "pages/contact.html")
