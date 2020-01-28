from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def myprofile(request):
    return render(request,'my profile.html')

def myhome(request):
    return render(request,'myhome.html')

def selfprofile(request):
    return render(request,'myprofile.html') 

def photos(request):
    return render(request,'photos.html')

def profiles(request):
    return render(request,'profiles.html')

def search(request):
    return render(request,'search.html')

def step1(request):
    return render(request,'step1.html')    

def step2(request):
    return render(request,'step2.html')  

def step3(request):
    return render(request,'step3.html')  

def step4(request):
    return render(request,'step4.html') 











def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirmpass']
        if password1 == password2:

            if User.objects.filter(email=email).exists():
                return render(request, 'index.html', {'error': 'username already exists'})
            else:

                user=User.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password1)
                Log_User=authenticate(username=email,password=password1)
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect(step1)
        else:
            return render(request, 'index.html', {'error': 'passwords not match'})
    else:
        return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect(myhome)
        else:
            return render(request, 'index.html', {'error': 'username and password incorrect'})
    else:
        return redirect(login)

def logout(request):
    auth.logout(request)
    return redirect('/')    