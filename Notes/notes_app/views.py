from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Note
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    data = Note.objects.filter(user_id=request.user.id)
    context = {"notes": data}
    return render(request, "notes_app/index.html", context=context)


@login_required
def add_note(request):
    title = str(request.POST["title"])
    if title:
        date = datetime.today()
        Note.objects.create(user_id=request.user.id, title=title, date=date)
    return redirect("home")


@login_required
def del_note(request, id):
    Note.objects.filter(user_id=request.user.id, id=id).delete()
    return redirect("home")


# Authentication
def login_user(request):
    msg = ""
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            msg = "Invalid username or password"
        return render(request, "notes_app/login.html", context={"msg": msg})

    return render(request, "notes_app/login.html")


def logout_user(request):
    logout(request)
    return redirect("login")


def signup(request):
    msg = ""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if username and password:
            if User.objects.filter(username=username).exists():
                msg = "Username is not available"
                return render(request, "notes_app/signup.html", context={"msg": msg})
            else:
                User.objects.create_user(username=username, password=password).save()
                return redirect("login")

    return render(request, "notes_app/signup.html")
