from django.shortcuts import render
from django.http import HttpResponse
from createcontent.models import Post
# Create your views here.

def userProfile(request):
    posts=Post.objects.filter(user=request.user).order_by("-created_at")
  
    return render(request,'profilepage/userProfile.html',context={'posts':posts})