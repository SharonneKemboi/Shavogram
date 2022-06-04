from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    image_url = models.ImageField(upload_to = 'pictures')
    name = models.CharField(unique = True,max_length = 31)
    caption = models.CharField(max_length = 50)
    likes = models.ManyToManyField(User, related_name = "likes")
    user = models.ForeignKey(User,on_delete=models.CASCADE,)

class Profile(models.Model):
    user = models.OneToOneField(User,related_name = "profile",on_delete=models.CASCADE,)
    bio = models.CharField(max_length = 40)
    picture = models.ImageField(upload_to = 'pictures')

class Comments(models.Model):
    photo = models.ForeignKey(Photo, related_name = "comments",on_delete=models.CASCADE,)
    user = models.ForeignKey(User, related_name = "comments",on_delete=models.CASCADE,)

class Follow(models.Model):
    user = models.ForeignKey(User, related_name = "followers", on_delete=models.CASCADE,)
    followed_by = models.ForeignKey(User, related_name = "following", on_delete=models.CASCADE,)     