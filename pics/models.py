from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=150, null=True, blank=True)
    profile_photo = models.ImageField(default='PHOTO', upload_to='profile_pics/')
    # followers = models.ForeignKey(Follow, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile_photo 

class Follow(models.Model):
    following = models.ForeignKey(User, related_name="who_follows", on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name="who_is_followed",on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user 

class Image(models.Model):
    photo = models.ImageField(upload_to = "images/",default='VALID PYTHON')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    photo_name = models.CharField(max_length = 30)
    likes = models.IntegerField(default=0)
    photo_caption = models.TextField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    photo_comments = models.IntegerField(default=0)


    def __str__(self):
    	return self.photo_name

class Comments(models.Model):
    text = models.TextField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Image ,on_delete=models.CASCADE)

    def __str__(self):
        return self.text

