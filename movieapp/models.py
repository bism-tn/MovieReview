from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator




class Movie(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)  
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )  

    


