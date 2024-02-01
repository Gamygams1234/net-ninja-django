from django.http import HttpResponse #last line below allows MyView.get 
# to return an HttpResponse object 
from django.views import View #View is to become the parent class of MyView
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("homepage")
    return render(request, "homepage.html")


def about(request):
    # return HttpResponse("about")
      return render(request, "about.html")

