from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup_view(request):
    # return HttpResponse("about")
    #   articles = Article.objects.all().order_by('date')
      form = UserCreationForm()
    #   the third parameter is a dictonarya
      return render(request, 'accounts/signup.html', {"form": form})