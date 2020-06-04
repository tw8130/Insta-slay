from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Comments,Image

class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		
		exclude = ['user','photo','date_posted']

class PostForm(forms.ModelForm):
  class Meta:
    model = Image
    
    exclude=['user']

    fields = ('photo_name', 'photo', 'photo_caption')

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SignInForm():
    email = forms.EmailField(label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
	model = Profile
	username = forms.CharField(label='Username',max_length = 30)
	
	bio = forms.CharField(label='Image Caption',max_length=500)
	profile_pic = forms.ImageField(label = 'Image Field')