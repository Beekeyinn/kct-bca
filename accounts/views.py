from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import login, authenticate, logout

from accounts.forms import LoginForm, UserCreationForm


# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password"),
            )
            if user:
                login(request, user)
                return redirect(reverse("post-list"))
            else:
                return render(
                    request,
                    "accounts/login.html",
                    {"errors": "User not Found", "form": form},
                )
        return render(request, "accounts/login.html", {"form": form})


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, "accounts/signup.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login"))
        return render(request, "accounts/signup.html", {"form": form})


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("login"))
