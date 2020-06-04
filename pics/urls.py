from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome, name='index'),
    path('search/', views.search_results, name='search_results'),
    path('upload/', views.upload , name='upload'),
    path('single_image/(\d+)',views.single_image, name='detail'),
    path('profile/', views.profile, name='profile'),
    path('upload_profile/', views.upload_profile, name='upload_profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)