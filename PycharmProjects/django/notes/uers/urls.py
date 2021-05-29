from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('regiter/', views.register, name= 'register'),
    path('profile/', views.profile, name= 'profile'),
    path('', views.main),
    path('editf/', views.edit_friends, name= 'profilef')
]
