from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from matriapp.forms import matriForm
from matriapp.models import Matridata,Castee,Subcastee,Heightt,Weightt,Starr,Raasii,Countryy,Statee,Cityy,Agee,Religionn


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
    cst = Castee.objects.all()
    subcst = Subcastee.objects.all()
    ht = Heightt.objects.all()
    return render(request,'step1.html',{'cste':cst,'sbcste':subcst,'heigt':ht})    
def step2(request):
    wt = Weightt.objects.all()
    strr = Starr.objects.all()
    Rs = Raasii.objects.all()
    cntry = Countryy.objects.all()
    st = Statee.objects.all()
    ct = Cityy.objects.all()
    return render(request,'step2.html',{'weight':wt,'starrr':strr,'rasi':Rs,'countryyy':cntry,'stateee':st,'cityyy':ct})  

def step3(request):
    return render(request,'step3.html')  

def step4(request):
    ag = Agee.objects.all()
    rgn = Religionn.objects.all()
    return render(request,'step4.html',{'ageee':ag,'religionnn':rgn}) 

# form function:

def matrisave(request):
    if request.method == 'POST':
        form = MatriForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(myprofile)
    else:
        form = Matriform()
        return render(request, 'index.html', {'form': form})


def edit(request, id):
    matri = Matridata.objects.get(id=id)
    return render(request, "edit.html", {'matri': matri})

def update(request, id):
    matri = Matridata.objects.get(id=id):
    form = MatriForm(request.POST, request.FILES, instance = matri)
    if form.is_valid():
        form.save()
        return redirect(myprofile)
    else:
        return render(request, "edit.html", {'matri': matri})

def delete(request, id):
    matri = Matridata.objects.get(id=id):
    matri.delete()
    return redirect(myprofile)










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
        if user is not None:
            auth_login(request, user)
            return redirect(myhome)
        else:
            return render(request, 'index.html', {'error': 'username and password incorrect'})
    else:
        return redirect(login)

def logout(request):
    auth_logout(request)
    return redirect('/')    