"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movieapp.views import UserRegistrationView,Signout,ReviewListView,LoginView,AddMovieView,AddReviewView,ShowMovieView,ShowMyReviewView,ShowReviewView,UpdateMovieView,UpdateReviewView,DeleteMovieView,DeleteReviewView,Home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ReviewApp/signup',UserRegistrationView.as_view(),name='signup'),
     path('ReviewApp/signout',Signout.as_view(),name='signout'),
   
    path('ReviewApp/login',LoginView.as_view(),name="login"),
    path('ReviewApp/addMovie',AddMovieView.as_view(),name="addmovie"),
    path('review/addReview',AddReviewView.as_view(),name="addreview"),
    
    path('ReviewApp/UpdateMovie/<int:pk>',UpdateMovieView.as_view(),name='updatemovie'),
    path('review/UpdateReview/<int:pk>',UpdateReviewView.as_view(),name='updatereview'),
    
    path('ReviewApp/DeleteMovie/<int:pk>',DeleteMovieView.as_view(),name='deletemovie'),
    path('ReviewApp/DeleteReview/<int:pk>',DeleteReviewView.as_view(),name='deletereview'),
    
    path('ReviewApp/ShowMovie',ShowMovieView.as_view(),name="allmovies"),
    path('ReviewApp/ShowReview',ShowReviewView.as_view(),name="allreviews"),
    path('ReviewApp/MyReview',ShowMyReviewView.as_view(),name="myreviews"),

    path('ReviewApp/home',Home.as_view(),name='home'),
    path('search/', ReviewListView.as_view(), name='searchreview'),
]
