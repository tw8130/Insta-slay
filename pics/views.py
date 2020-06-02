from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Image , Follow
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

        return render(request, 'search_pic.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_pic.html',{"message":message})

@login_required(login_url='/accounts/login/')
def single_image(request,photo_id):
	photo = Image.objects.get(id= photo_id)

	return render(request, 'all-pics/profile_detail.html',{"photo":photo})

@login_required(login_url='/accounts/login/')
def comment(request,id):
	
	post = get_object_or_404(Image,id=id)	
	current_user = request.user
	print(post)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = current_user
			comment.photo = post
			comment.save()
			return redirect('index')
	else:
		form = CommentForm()

	return render(request,'all-pics/comment.html',{"form":form})  


@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.profile_pic = form.cleaned_data['profile_pic']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_pic = form.cleaned_data['profile_pic'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()


    return render(request,'all-pics/upload_profile.html',{"title":title,"current_user":current_user,"form":form})

@login_required(login_url='/accounts/login/')
def profile(request):
	current_user = request.user
	profile = Profile.objects.all()
	follower = Follow.objects.filter(user=profile).count()

	return render(request, 'all-pics/user_profile.html',{"current_user":current_user,"profile":profile,"follower":follower,"following":following})