"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('home/dele/', views.bele),
    path('admin/', admin.site.urls),
path('home/<str:pk>/<str:pk2>/<str:pk3>', views.getdocx),
path('home/in/<str:pk>/<str:pk2>/<str:pk3>', views.getpdf),
    path('in/<str:pk>/<str:pk2>/<str:pk3>', views.getpdf),
    path('index', views.index),
    path('test/', views.test),
   # path('home/', views.model_form_upload),
    path('', include('uers.urls')),
    path('login/', auth_views.LoginView.as_view(template_name = 'uers/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'uers/logout.html'), name='logout'),
    path('home/', views.index, name='home'),
    path('right/', views.right_index),
    path('', include('social.urls')),
    path(r'^friendship/', include('friendship.urls')),
    path('test/', views.test),
path('cha', views.edi_change, name='change_about'),
    path('home/book_summjary/<int:value>', views.test_sum, name='book_summary'),




]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)