from django.shortcuts import render

from createcontent.views import Postview 
from createcontent.models import Post
from django.contrib.auth.decorators import login_required
@login_required(login_url="/login/")
def Home(request):
    if request.method=="POST" and request.POST['submit']=="POST":
        Postview(request)

    return render(request,'homepage.html',context={"posts":Post.objects.all().order_by('-created_at')})
