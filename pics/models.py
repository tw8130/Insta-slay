from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=150, null=True, blank=True)
    profile_photo = models.ImageField(default='PHOTO', upload_to='profile_pics/')
    # followers = models.ForeignKey(Follow, on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    def update_profile(self,update):
        self.profile_photo = update
        self.save()

    def __str__(self):
        return self.bio 

    @classmethod
    def search_by_user(cls,search_term):
        photo = cls.objects.filter(user__icontains=search_term)
        return photo  

    @classmethod
    def get_all_users(cls):
        all_users = Profile.objects.all()
        return all_users 
    

class Follow(models.Model):
    following = models.ForeignKey(User, related_name="who_follows", on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name="who_is_followed",on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def save_follow(self):
        self.save()

    def delete_follow(self):
        self.delete()

    def __str__(self):
        return self.user
    

class Image(models.Model):
    photo = models.ImageField(upload_to = "images/",default='VALID PYTHON')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    photo_name = models.CharField(max_length = 30)
    likes = models.CharField(max_length=20, blank=True)
    photo_caption = models.TextField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    # profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, blank=True)
    photo_comments = models.CharField(max_length=150)

    class Meta:
        ordering = ['-pub_date']

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_caption(self,update):
        self.photo_caption = update
        self.save()
    
    def __str__(self):
        return self.photo_caption

    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
    
    @classmethod
    def get_image_by_id(cls, id):
        the_image = Image.objects.get(id =id)
        return the_image
    
class Comments(models.Model):
    text = models.TextField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo= models.ForeignKey(Image, on_delete=models.CASCADE,related_name='comment',default='3')

    def __str__(self):
        return self.text
    
    def delete_comments(self):
        self.delete()
    
    def save_comments(self):
        self.save()
    
    def update_comments(self,update):
        self.text = update
        self.save()
