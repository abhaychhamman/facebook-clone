from django.shortcuts import render

# Create your views here.
def friendsPage(request):
    return render (request,'friendsPage/friendsPage.html')