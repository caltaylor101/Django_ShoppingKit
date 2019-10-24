from django.db import models
from kit.models import KitPost
from django.urls import reverse

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=500)
    image = ProcessedImageField(upload_to='category_photo',
                                           processors=[ResizeToFill(500, 500)],
                                           format='JPEG',
                                           options={'quality': 100})
    def __str__(self): 
        return self.name

   
    class Meta: 
        ordering = ['name']




    

#Possible vulnerability in the password field. Fix this later. 
#Eventually update so that it's not password based, but invite / request for invite based. 
class Private_Category(models.Model):
    owner = models.ForeignKey(User, related_name='privateowner', on_delete=models.CASCADE, null=True)
    category_password = models.CharField(max_length=50)

    #authenticated_users is a temporary solution creating a list of authenticated users once
    #they know the password to the private category.
    
    title = models.CharField(max_length=200, unique = True)
    description = models.CharField(max_length=500)
    image = ProcessedImageField(upload_to='category_photo',
                                           processors=[ResizeToFill(500, 500)],
                                           format='JPEG',
                                           options={'quality': 100})
    def __str__(self): 
        return self.title


class Private_Users(models.Model): 
    name = models.CharField(max_length=50, null=True)
    
    category = models.ForeignKey(Private_Category, null=False, on_delete=models.CASCADE, default=None)

    def __str__(self): 
        return self.name


    

    




    

