from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index (request):
    return render(request,'index.html')

"""def login (request):
    return render(request, 'login.html')"""

def detail_view(request):
    return render(request,'detail_view.html')

"""def BasicDetails (request):
    if request.method=="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        fathername = request.POST.get('fathername')
        mothername = request.POST.get('mothername')
        dateofbirth = request.POST.get('dateofbirth')
        gender = request.POST.get('gender')
        about = request.POST.get('about')
        coursename = request.POST.get('coursename')
        universityname = request.POST.get('universityname')
        passingyear = request.POST.get('passingyear')
         print(firstname, lastname,fathername,mothername,dateofbirth,gender,about,coursename,universityname,passingyear)

        # check if user has entered correct credentials
        user = authenticate(firstname=firstname, lastname=lastname,fathername=fathername,mothername=mothername,dateofbirth=dateofbirth,gender=gender,about=about,coursename=coursename,universityname=universityname,passingyear=passingyear)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')"""
def BasicDetails (request):
    return render(request, 'login.html')
