from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def signup_view(request):
    # return HttpResponse("about")
    #   articles = Article.objects.all().order_by('date')
      return render(request, 'accounts/signup.html')