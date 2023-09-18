import json

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import std_form,department,course
from .form import regform_form

# Create your views here.
def index(request):
    return render(request,"index.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            std_id = user.id
            return redirect('click',std_id=std_id)
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")

@login_required
def click(request,std_id):
    user = User.objects.get(id=std_id)
    return render(request,"click.html",{'user':user})


@login_required
def std_form(request):
    if request.method == 'POST':
        form = regform_form(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Your form was submitted successfully")
        else:
            messages.info(request, "Invalid form submission")
    else:
        form = regform_form()

    return render(request, "reg_form.html", {'forms': form})
def getcourse(request):
    data = json.loads(request.body)
    department_id = data["id"]
    courses = course.objects.filter(department_id=department_id)
    return JsonResponse(list(courses.values("id","name")),safe=False)
