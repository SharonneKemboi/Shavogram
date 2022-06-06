from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Photo(models.Model):
    image_url = models.ImageField(upload_to = 'pictures' , blank = True)
    name = models.CharField(max_length = 35, blank = True)
    caption = models.CharField(max_length = 55, blank = True)
    likes = models.ManyToManyField(User, related_name = "likes", blank = True)
    user = models.ForeignKey(User, related_name = "posts", on_delete=models.CASCADE, blank=True)
    pub_date = models.DateTimeField(auto_now_add = True, blank = True)
    
    def __str__(self):
        return self.name

    def save_photo(self):
        self.save()

  
    def delete_photo(self):
      Photo.objects.get(id = self.id).delete()

    def update_caption(self,new_caption):
        self.caption = new_caption
        self.save()

class Profile(models.Model):
    user = models.OneToOneField(User,related_name = "profile",on_delete=models.CASCADE,)
    bio = models.CharField(default="Welcome", max_length = 40)
    picture = models.ImageField(upload_to = 'pictures', blank = True)


   
    def __str__(self):
        return f'{self.user.username} Profile'
        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    @classmethod
    def search_user(cls,name):
        return User.objects.filter(username__icontains = name)

class Comments(models.Model):
    mycomments = models.TextField(max_length = 100, blank = True)
    photo = models.ForeignKey(Photo, related_name = "comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name = "comments",on_delete=models.CASCADE)
   

    def save_comment(self):
        self.save()

    def delete_comment(self):
        Comments.objects.get(id = self.id).delete()
    
    def update_comment(self,new_comment):
        mycomments = Comments.objects.get(id = self.id)
        mycomments.comment = new_comment
        mycomments.save()
   
    def __str__(self):
        return f'{self.user.comments} Photo'

   
   

class Follow(models.Model):
    user = models.ForeignKey(User, related_name = "user_followers", on_delete=models.CASCADE,)
    followed_by = models.ForeignKey(User, related_name = "user_following", on_delete=models.CASCADE,)   

    def __str__(self):
        return f'{self.followed_by} Follow'

class identifiers(models.Model):
    identifier = models.CharField(max_length = 30, null = True)    

    def __str__(self):
        return f'{self.identifier} identifiers'