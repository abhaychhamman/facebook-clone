 
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('createpost', views.Postview ,name="createpost"),
    path('showcomments/', views.showcomments ,name="showcomments"),
    path('postComment/', views.postComment ,name="postComment"),
   
 

]
