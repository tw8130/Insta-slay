from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile, Image , Follow
from django.contrib.auth.models import User
from .forms import PostForm,CommentForm,ProfileUploadForm,RegistrationForm,SignInForm


# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):
   all_images = Image.objects.all()
   all_users = Profile.objects.all()
   title = 'Instagram'
#    next = request.GET.get('next')
#    if next: return redirect(next)

   current_user = request.user
   if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
                comment = form.save(commit=False)
                comment.user = current_user
                comment.save()
        return redirect('index')
   else:
            form = CommentForm()

   return render (request,'welcome.html' ,{'title':title,'all_images':all_images,"form":form ,"current_user":current_user,"all_users":all_users} )

# @login_required(login_url='/accounts/login/')
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
    form = SignInForm()
    return render(request, 'registration/login.html', {'form': form})


#Log-Out page view function
def logout(request):
    return render(request, 'registration/logout.html')

def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'search_pic.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search_pic.html',{"message":message})

# @login_required(login_url='/accounts/login/')
def single_image(request,photo_id):
	photo = Image.objects.get(id= photo_id)

	return render(request, 'all-pics/profile_detail.html',{"photo":photo})

# @login_required(login_url='/accounts/login/')
# def comment(request):
	
# 	# post = Image.objects.get(id=photo_id)	
# 	current_user = request.user
# 	# print(post)

# 	if request.method == 'POST':
# 		form = CommentForm(request.POST ,request.FILES)

# 		if form.is_valid():
# 			comment = form.save(commit=False)
# 			comment.user = current_user
# 			# comment.photo = post
# 			comment.save()
# 			return redirect('index')
# 	else:
# 		form = CommentForm()

# 	return render(request,'all-pics/comment.html',{"form":form})  


# @login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.profile_photo = form.cleaned_data['profile_photo']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.user = form.cleaned_data['user']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_photo = form.cleaned_data['profile_photo'],bio = form.cleaned_data['bio'],user = form.cleaned_data['user'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()


    return render(request,'all-pics/upload_profile.html',{"title":title,"current_user":current_user,"form":form})

# @login_required(login_url='/accounts/login/')
def profile(request):
	current_user = request.user
	profile = Profile.objects.all()
	follower = Follow.objects.filter(user=profile)

	return render(request, 'all-pics/user_profile.html',{"current_user":current_user,"profile":profile,"follower":follower})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Thank you, {username}. Your account has been created')
            return redirect('login')

    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})