 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .models import Post,friendsModal,DoPOST
from authentication.models import Profile

@csrf_exempt
def Postview(request):
    print(request.POST['submit'])
   
    pst=Post(user=request.user,description=request.POST['desc'],img_vid=request.FILES['img_vid'],feeling="happy")
    pst.save()



from datetime import datetime      
@csrf_exempt
def showcomments(request):

    print(request.POST) #required but i don't no
    p=Post.objects.get(id=request.POST['id'])
    d=DoPOST.objects.filter(post=p)
    
    lst=[{"comments_content":i.comments,"commentUsername":i.commentsUsername,"created_at":i.created_at.date()} for i in d.order_by('-created_at')][:int(request.POST['Ncomment'])]
    return JsonResponse({"data":lst,"commentCounter":p.commentCounter})
 
@csrf_exempt
def postComment(request):
    r=request.POST
    p=Post.objects.get(id=r.get('postId'))
    d=DoPOST.objects.create(post=p,comments=r.get("postCommentContent"),commentsUsername=Profile.objects.get(username=request.user).fname)
    d.save()
    p.commentCounter=len(DoPOST.objects.filter(post=p))
    p.save()
    
    data={"comments_content":d.comments,"commentUsername":d.commentsUsername,"commentCounter":p.commentCounter,"created_at":d.created_at.date()}
    return JsonResponse({"data":data})
 
