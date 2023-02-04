from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .models import Profile

from createcontent.models import friendsModal
# Create your views here.



def Login(request):
  
    if request.method == 'POST' and request.POST['submit']=="Sign Up":  
          
            nuser=len(User.objects.all())
            c=Profile(username=request.POST['fname']+str(nuser),fname=request.POST['fname'],sname=request.POST['sname'],email=request.POST['email'],password=request.POST['password'],gender=request.POST['gender'],dob=request.POST['dob'])
            c.save()
           
            print(request.POST)
        
            return HttpResponseRedirect('/')
  
    if request.method == 'POST' and request.POST['submit']=="Log in":  

            c=Profile.objects.get(email=request.POST['email'])
            print(c.username)
            user=authenticate(username=c.username,password=request.POST['password']) 
            print(user,request.POST['email'],request.POST['password'])
            if user is not None:
                login(request,user)
                print(request.user.is_authenticated)
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('/login/')

    return render(request,"login.html")
    

def logout_page(request):
    logout(request)
    return    HttpResponseRedirect('/login/')
  

       
def friendsView(request):

    context={"usersWithFrConnection":friendsModal.objects.all()}


    return render(request,"friendsView.html",context=context)