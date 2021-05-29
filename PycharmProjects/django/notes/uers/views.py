from django.shortcuts import render, redirect
from friendship.models import FriendshipRequest,Friend,Block
from django.contrib import messages
from .forms import UserRegisterForm,ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.

from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"account created for {username}")
            return redirect('/test/')
    else:
        form = UserRegisterForm()

    return render(request,'uers/register.html',{'form': form})
@login_required
def profile(request):
    if request.method == 'POST':
       # u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():
           # u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
       # u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
     #   'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'uers/profile.html', {'pform': p_form})

def main(request):
    freq =  Friend.objects.requests(user=request.user)



    return render(request,'Main_truct.html',{'freq': freq})

def edit_friends(request):
    fri = Friend.objects.friends(request.user)

    if request.method =="POST":
        pk = request.POST["fri_name"]
        to_user = User.objects.get(username=pk)
        if 'fri_bt1' in request.POST:
            Block.objects.add_block(request.user,to_user)

        if 'fri_bt3' in request.POST:
            Block.objects.remove_block(request.user, to_user)

        if 'fri_bt2' in request.POST:
            Friend.objects.remove_friend(request.user,User.objects.get(username=request.POST['fri_name']))



    return render(request,"uers/editfriends.html", {'fri':fri})





