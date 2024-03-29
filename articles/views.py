from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def article_list(request):
    # return HttpResponse("about")
      articles = Article.objects.all().order_by('date')
      return render(request, "articles/article_list.html", {'articles': articles})

def article_detail(request, slug):
    # return HttpResponse("about")

    #   return HttpResponse(slug)
      article = Article.objects.get(slug=slug)
      return render(request, "articles/article_detail.html", {'article': article})


@login_required(login_url="/accounts/login/")
def article_create(request):
    # return HttpResponse("about")
      if request.method == "POST":
          form = forms.CreateArticle(request.POST, request.FILES)
          if form.is_valid():
               instance=form.save(commit=False)
               instance.author = request.user
               instance.save()
               return redirect("articles:list")
      else:
    #   return HttpResponse(slug)
          form = forms.CreateArticle()
          return render(request, "articles/article_create.html", {"form" : form})
