from django.shortcuts import render, redirect
from .form import editpost
from django.http import HttpResponse
from .models import posts,book_reck,post
from django.contrib import messages
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
from friendship.models import FriendshipRequest
from friendship.models import FriendshipRequest

from django.contrib.auth.decorators import login_required


@login_required
def friend_accept(request):
   friend_request = FriendshipRequest.objects.get(to_user=1)
   friend_request.accept()
   return
# or friend_request.reject()
@login_required
def friendship_add(request):

   if request.method == 'POST':
      pk = request.POST["friend_id"]
      to_user = User.objects.get(username=pk)
      from_user = request.user

      Friend.objects.add_friend(from_user, to_user)
      return HttpResponse('You added a friend')

   return render(request, 'wall.html')
@login_required
def requestacc(request):
   if request.method == 'POST':
      pk = request.POST["freqq"]
      if "axx" in request.POST:
         try:
            friend_request = FriendshipRequest.objects.get(from_user =pk)
            friend_request.accept()
         except:
            return HttpResponse("Already accepted")
      if "reject" in request.POST:
         friend_request = FriendshipRequest.objects.get(from_user=pk)
         friend_request.reject()
   return HttpResponse("acc")
@login_required
def wall(request):

   allpc = post.objects.all()
   allp = posts.objects.order_by('-id')
   fri = Friend.objects.friends(request.user)
   friend_request = Friend.objects.unrejected_requests(user=request.user)
   allrec = book_reck.objects.filter(buser = 3)

   if request.method == 'POST':
         k = request.POST["fname"]
         allp = posts.objects.filter(user = request.POST[f"{k}"])

   return  render(request, "wall.html",{'allp':allp, 'allrec':allrec,'freq':friend_request, 'fri':fri, 'allpc': allpc})

@login_required
def edit(request):
     if request.method=="POST":
        sobj=posts()
        sobj.user = request.user
        sobj.psub=   request.POST["t2"]
        sobj.pdes=request.POST["t3"]
        sobj.ptags=request.POST["t4"]
        sobj.save()
        return render(request,'newpost.html',{'records':posts.objects.all()})
     else:
        return render(request,'newpost.html')
@login_required
def reqpage(request):
   return render(request, 'friendreq.html')
@login_required
def recomend(request):
   if request.method == "POST":
      bobj = book_reck()
      bobj.buser = User.objects.get(username=request.POST["t3"])
      bobj.bdes = request.POST["t2"]
      bobj.pname = request.POST["t4"]
      bobj.save()
      return HttpResponse("die biwh")
   else:
      return render(request, "bokrec.html")
@login_required
def recomend_all(request):
   if request.method == "GET":
      bobj = book_reck()
      bobj.buser = User.objects.get(username=request.user)
      bobj.bid = request.POST["book_id"]


      bobj.save()
      return HttpResponse("die biwh")
   else:
      return render(request, "bokrec.html")

@login_required
def editpost(request):
   sobj = posts.objects.filter(user= request.user)
   return render(request,'uers/editposts.html',{'editp':sobj})

@login_required
def comment_Test(request):
   if request.method == 'POST':
      allpc = post()
      allpc.post = posts.objects.get(id =  request.POST["t1"])
      allpc.likes = request.POST["t2"]
      allpc.pcomment = request.POST["t3"]
      allpc.save()
      return HttpResponse("kuch nih his")
   else:
      return render(request,"comment.html")
# Create your views here.

def add_bookmark(request, id):
   bpost = posts()
   posts.objects.filter(id=id).update(bku=request.user)
   return HttpResponse("now")


def edit_marks(request):
   k=  posts.objects.filter( bku = request.user)


   return render(request, "uers/editbookmarks.html", {'fri': k})

