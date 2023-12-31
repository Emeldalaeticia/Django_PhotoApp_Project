from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# from taggit.managers import TaggableManager

class Photo(models.Model):

    title = models.CharField(max_length=45)

    description = models.CharField(max_length=250) 

    created = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='photos/')

    submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # tags = TaggableManager() 
    likes = models.ManyToManyField(User, related_name='liked_photos')

    def __str__(self):
        return self.title