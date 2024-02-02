from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.


def signup_view(request):

      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              
               form.save()
               user = form.get_user()
               login(request, user)
            #    log user in
               return redirect("articles:list")
      else:
          form = UserCreationForm()
      return render(request, 'accounts/signup.html', {"form": form})   

# do not user the function to login
def login_view(request):

      if request.method == "POST":
          form = AuthenticationForm(data=request.POST)
          if form.is_valid():
            #    log user in
               user = form.get_user()
               login(request, user)
               if "next" in request.POST:
                    return redirect(request.POST.get('next'))
               else:
                    return redirect("articles:list")
      else:
          form =  AuthenticationForm()
      return render(request, 'accounts/login.html', {"form": form})   


def logout_view(request):

      if request.method == "POST":
          logout(request)

          return redirect("articles:list")
 
