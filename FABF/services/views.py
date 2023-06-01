from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from services.models import User, Role

# Create your views here.

def index(request):
    return render(request, 'index.html', context={})

def register(request):
    roles = Role.objects.all()
    return render(request, 'register/index.html', context={'roles': roles})

def add_user(request):
    lastName = request.POST.get('lastName')
    firstName = request.POST.get('firstName')
    birthPlace = request.POST.get('birthPlace')
    birthDate = request.POST.get('birthDate')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    userName = request.POST.get('userName')
    password = request.POST.get('password')
    rePassword = request.POST.get('rePassword')
    gender = request.POST.get('gender')
    role = request.POST.get('role')
    if lastName=='' or firstName=='' or birthPlace=='' or birthDate==''or phone=='' or email=='' or userName=='' or password=='' or rePassword=='' or gender=='' or role=='':
        return render(request, 'register/index.html', context={
                    'error': 'Veuillez renseigner tous les champs.'
                })
    else:
        if password != rePassword:
            return render(request, 'add_user.html', context={
                        'error': 'Les mots de passe ne correspondent pas.'
                    })
        else:
            user = User.objects.create(userName=userName, password=password, email=email, firstName=firstName, lastName=lastName, birthPlace=birthPlace, birthDate=birthDate, phone=phone, gender=gender, role=role)
            user.save()
            return HttpResponseRedirect('/login')
    
    #return HttpResponse("Welcome register")

def login(request):
    return render(request, 'login/index.html', context={})
        #return HttpResponse("Welcome login")