from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm


def register_view(request):
    form = RegisterForm(request.post or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password1 = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(email, password1)
        except:
            user = None
        if user:
            login(request, user)
        else:
            request.session['register_error'] = 1
    return render(request, "forms.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['invalid_user'] = 1
    return render(request, "forms.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('/login')