from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    path('wall/', views.wall, name='wall'),
    path('edit/', views.edit,name='edit'),
    path('editp/', views.editpost),
path('fr_request_acc/', views.requestacc, name='fr_request_acc'),
    path('fr_request/', views.friendship_add, name='fr_request'),
    path('freq/' ,views.reqpage),
    path('breq/', views.recomend, name="breq"),
    path('home/breq/', views.recomend_all),
path('test_comment', views.comment_Test,name='test_comment'),
path('bookmark/<int:id>', views.add_bookmark),
path('editbookmark', views.edit_marks,name='marks'),



]
