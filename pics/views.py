from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
   title = 'PetyInstagram'
   image_posts = Image.objects.all()
   return render (request,'welcome.html' ,{'title':title, 'image_posts':image_posts})