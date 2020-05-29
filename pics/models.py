from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to = "images/",null = True)
    user = models.ForeignKey(User,null=True)
    photo_name = models.CharField(max_length = 30,null = True)
    likes = models.IntegerField(default=0)
    photo_caption = models.TextField(null = True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    comments = models.TextField(default=0)


    def __str__(self):
    	return self.pic_name
