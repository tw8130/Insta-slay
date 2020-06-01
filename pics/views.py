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
   return render (request,'all-pics/welcome.html' ,{'all_images':all_images, 'all_users':all_users})

@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    p = Profile.objects.filter(id=current_user.id).first()
    user = Image.objects.filter(user=p).all()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user= p
            post.save()
            return redirect('/')
    else:
        form =PostForm
    return render(request, 'all-pics/upload.html', {"form": form})

#Login page view function
def login(request):
    return render(request, 'django_registration/login.html')

#Log-Out page view function
def logout(request):
    return render(request, 'django_registration/logout.html')

def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search_pic.html',{"message":message,"profile": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_pic.html',{"message":message})
