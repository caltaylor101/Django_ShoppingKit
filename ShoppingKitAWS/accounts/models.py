from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from vote.models import VoteModel

# Create your models here.

#UserProfileManager manages the query sets so we don't have to
#Query things over and over again.
class UserProfileManager(models.Manager):
        def get_queryset(self):
                return super(UserProfileManager, self).get_queryset().filter(city='San Diego')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length = 100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

    image = models.ImageField(upload_to='profile_image', blank=True)

    SanDiego = UserProfileManager()
    objects = models.Manager()



    def __str__(self): 
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']: 
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class Profile(VoteModel, models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
