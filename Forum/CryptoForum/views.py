from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .models import *
from .forms import *


def home(request):
    forums = Forum.objects.all()
    count = forums.count()
    comments = []
    for i in forums:
        comments.append(i.comments_set.all())

    context = {'forums': forums,
               'count': count,
               'comments': comments}
    return render(request, 'home.html', context)

def addInForum(request):
    if request.user.is_authenticated:
        form = CreateInForum()
        if request.method == 'POST':
            form = CreateInForum(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'addInForum.html', context)
    else:
        return redirect('/accounts/login')

def addInComments(request):
    form = CreateInComments()
    if request.method == 'POST':
        form = CreateInComments(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'addInComments.html', context)

def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))
