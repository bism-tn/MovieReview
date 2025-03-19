from django.shortcuts import render, redirect
from movieapp.models import User, Movie, Review
from movieapp.forms import Userform, LoginForm, Movieform, ReviewForm
from django.views.generic import View, ListView
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.db.models import Q


def is_login(fn):
    def wrapper(request, *args, **kwargs):  
        if not request.user.is_authenticated:
            return redirect("login")
        return fn(request, *args, **kwargs)  
    return wrapper

def is_user(fn):
    def wrapper(request, *args, **kwargs):
        id = kwargs.get("pk")
        data = Review.objects.get(id=id)
        if data.user == request.user:
            return fn(request, *args, **kwargs)
        return redirect("login")
    return wrapper


class UserRegistrationView(View):
    def get(self, request):
        form = Userform()
        return render(request, "signup.html", {"form": form})
    
    def post(self, request):
        form = Userform(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login")
        return render(request, "signup.html", {"form": form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        u_name = request.POST.get("username")
        pwd = request.POST.get("password")

        user_obj = authenticate(request, username=u_name, password=pwd)
        if user_obj:
            login(request, user_obj)
            return redirect("home")
        return render(request, "login.html", {"form": form, "error": "Invalid credentials"})


class Signout(View):
    def get(self, request):
        logout(request)
        return redirect("login")

@method_decorator(is_login, name='dispatch')
class AddMovieView(View):
    def get(self, request):
        form = Movieform()
        return render(request, "addmovie.html", {"form": form})

    def post(self, request):
        form = Movieform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("allmovies")
        return render(request, "addmovie.html", {"form": form})

@method_decorator(is_login, name='dispatch')
class ShowMovieView(View):
    def get(self, request):
        data = Movie.objects.all()
        return render(request, "showmovie.html", {"form": data})

@method_decorator(is_login, name='dispatch')
class UpdateMovieView(View):
    def get(self, request, pk):
        data = Movie.objects.get(id=pk)
        form = Movieform(instance=data)
        return render(request, "updatemovie.html", {"form": form})

    def post(self, request, pk):
        data = Movie.objects.get(id=pk)
        form = Movieform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("allmovies")
        return render(request, "updatemovie.html", {"form": form})

@method_decorator(is_login, name='dispatch')
class DeleteMovieView(View):
    def get(self, request, pk):
        Movie.objects.get(id=pk).delete()
        return redirect("allmovies")

@method_decorator(is_login, name='dispatch')
class AddReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "addreview.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Assign the logged-in user
            review.save()
            return redirect("myreviews")
        return render(request, "addreview.html", {"form": form})

@method_decorator(is_login, name='dispatch')
class ShowReviewView(View):
    def get(self, request):
        data = Review.objects.all()
        return render(request, "showreview.html", {"form": data})

@method_decorator(is_login, name='dispatch')
class ShowMyReviewView(View):
    def get(self, request):
        data = Review.objects.filter(user=request.user)
        return render(request, "Myreview.html", {"form": data})

@method_decorator([is_login, is_user], name='dispatch')
class UpdateReviewView(View):
    def get(self, request, pk):
        data = Review.objects.get(id=pk)
        form = ReviewForm(instance=data)
        return render(request, "updatereview.html", {"form": form})

    def post(self, request, pk):
        data = Review.objects.get(id=pk)
        form = ReviewForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("myreviews")
        return render(request, "updatereview.html", {"form": form})

@method_decorator([is_login, is_user], name='dispatch')
class DeleteReviewView(View):
    def get(self, request, pk):
        Review.objects.get(id=pk).delete()
        return redirect("myreviews")

class Home(View):
    def get(self, request):
        return render(request, 'home.html')


@method_decorator(is_login, name='dispatch')
class ReviewListView(ListView):
    model = Review
    template_name = 'showreview.html'  
    context_object_name = 'form'  
    ordering = ['-created_at']  

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Review.objects.filter(Q(movie__name__icontains=query))  
        return Review.objects.all()
