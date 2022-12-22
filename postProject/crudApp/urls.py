from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/add/', views.addPost, name='addPost'),
    path('posts/', views.postt, name='postt'),
    path('post/view/<int:pk>', views.postDetail, name='postDetail'),
    path('post/delete/<int:pk>', views.deletePost, name='deletePost'),
    path('post/edit/<int:pk>', views.editPost, name='editPost'),
    path('sign-up/', views.signUp, name='signUp'),
    path('log-in/', views.logIn, name='logIn'),
    path("logout/", views.logoutUser, name= "logoutUser"),
]