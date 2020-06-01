from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Image
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
   all_images = Image.objects.all()
   all_users = Profile.objects.all()
   next = request.GET.get('next')
   if next: return redirect(next)
   return render (request,'welcome.html' ,{'all_images':all_images, 'all_users':all_users})

@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    p = Profile.objects.filter(id=current_user.id).first()
    user = Image.objects.filter(user=p).all()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.imageuploader_profile= p
            post.save()
            return redirect('/')
    else:
        form =PostForm
    return render(request, 'all_pics/upload.html', {"form": form})

#Login page view function
def login(request):
    return render(request, 'django_registration/login.html')

#Log-Out page view function
def logout(request):
    return render(request, 'django_registration/logout.html')


