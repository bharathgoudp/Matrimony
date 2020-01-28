from django.shortcuts import render

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