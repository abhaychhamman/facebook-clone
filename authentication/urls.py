 
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('login/', views.Login ,name="Login"),
    path('logout/', views.logout_page ,name="logout"),
    path('friendsView', views.friendsView ,name="friendsView"),
     
 

]
