from django.db import models
from django.contrib.auth.models import User
from authentication.models import Profile
from datetime import datetime


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    description=models.TextField(default="very Powerful Content")
    feeling= models.TextField(default="news")
    img_vid=models.ImageField(upload_to="media/post/",default='')
    likes=models.CharField( max_length=100,default="0")
    share=models.CharField( max_length=100,default="0")
    commentCounter=models.CharField( max_length=50,default="0")
    created_at =  models.DateTimeField(default=datetime.now)
    def __str__(self):
        return str(self.user )+ str(self.id)

class DoPOST(models.Model): 
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    comments=models.CharField( max_length=500)
    commentsUsername=models.CharField( max_length=70,default="admin")
    created_at =  models.DateTimeField(default=datetime.now)
 

    def __str__(self):
        return self.post.user.first_name+str(self.post.id)

# Create your models here.
class friendsModal(models.Model):
    user = models.ForeignKey(Profile , on_delete=models.CASCADE)
    friends = models.ManyToManyField(
        "self",
        symmetrical=True,
        blank=True
    )
  
    def __str__(self):
        return str(self.user.fname)+" "+str(self.user.sname)
 
    
    