from django import forms
from movieapp.models import User,Movie,Review


class Userform(forms.ModelForm):
    class Meta:

        model = User
        fields = ["username","first_name","last_name","password","email"]
        widgets={
            'username' : forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the Username"}),
            'first_name' : forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the first name"}),
            'last_name' : forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the last name"}),
            'password' : forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter the password"}),
            'email' : forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter the email"})
        }
class LoginForm(forms.Form):
     

     username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the name"}))
     password=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the password"}))

class Movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["name","language","release_date","genre","director"]
        labels = {
            "name": "Movie Name",
            "language": "Language",
            "release_date": "Release Date",
            "genre": "Genre",
            "director": "Director",
        }
        
        widget={
            'name':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the name"}),
            'language':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the language"}),
            'release_date':forms.DateInput(attrs={"class":"form-control","placeholder":"Enter the Date"}),
            'director':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the Director"})
        }

class ReviewForm(forms.ModelForm):
    
    movie = forms.ModelChoiceField(
        queryset=Movie.objects.all(),  
        empty_label="Select a movie"
    )

    class Meta:
        model = Review
        fields = ['movie', 'comment', 'rating']
        labels = {
            'movie':"Movie",
            'Comment':'Comment',
            'rating':'Rating'

        }
    
