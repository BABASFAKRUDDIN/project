
from django.db import models

# Create your models here.
Gender= (
    ("M", "Male"),
    ("F", "Female")
    )
class Director(models.Model):
    
    name=models.CharField(max_length=100,unique=True)
    date_of_birth=models.DateField(null=True)
    gender=models.CharField(max_length=6,choices=Gender)
    description=models.TextField(null=True)
    poster=models.ImageField(null=True)
    no_of_facebook_likes=models.IntegerField(null=True)

class Actor(models.Model):
    actor_id=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True)
    gender=models.CharField(max_length=6,choices=Gender,null=True)
    description=models.TextField(null=True)
    poster=models.ImageField(null=True)
    fb_likes=models.IntegerField(null=True)

class Movie(models.Model):
    Status=(
        ("Block Buster",'B'),
        ('Average','A'),
        ('Disaster','D')
    )
    name=models.CharField(max_length=100)
    movie_id=models.CharField(max_length=100,primary_key=True)
    release_date=models.IntegerField(null=True)
    box_office_collection_in_crores=models.FloatField()
    director=models.ForeignKey(Director,on_delete=models.CASCADE)
    actors=models.ManyToManyField(Actor,through="Cast")
    poster=models.ImageField(null=True)
    description=models.TextField(null=True)
    result=models.CharField(max_length=12,choices=Status,null=True)
    genre=models.CharField(max_length=50,null=True)
    fb_likes=models.IntegerField(null=True)
    country=models.CharField(max_length=100,null=True)
    average_rating=models.FloatField(null=True)
    language=models.CharField(max_length=50,null=True)
    no_of_users_voted=models.IntegerField(null=True)

    
class Cast(models.Model):
    actor=models.ForeignKey(Actor,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    role=models.CharField(max_length=50)
    is_debut_movie=models.BooleanField(default=False,null=True)
    Remuneration=models.FloatField(default=0,null=True)
    
class Rating(models.Model):
    movie=models.OneToOneField(Movie,on_delete=models.CASCADE)
    rating_one_count=models.IntegerField(default=0)
    rating_two_count=models.IntegerField(default=0)
    rating_three_count=models.IntegerField(default=0)
    rating_four_count=models.IntegerField(default=0)
    rating_five_count=models.IntegerField(default=0)
