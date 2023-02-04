
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
from createcontent.models import friendsModal,Post
 
 
@receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    print("ni hao",sender)
    if created:
        c=User.objects.create_user(username=instance.username,email=instance.email,password=instance.password)
        c.first_name = instance.fname
        c.last_name = instance.sname
        c.save()
        friendsModal.objects.create(user=instance)
        print(f'{"all set":-^50}')
 