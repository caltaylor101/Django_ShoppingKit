from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model): 
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #saves the date of data it was initially entered with, not updated with. 
    created = models.DateTimeField(auto_now_add=True)
    #saves when the data was updated. 
    updated = models.DateTimeField(auto_now=True)


#Eventually use this type of model relationship for private categories. 
class Friend(models.Model): 
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, null=True)


    #Always use self for the first argument to instance methods.
    #Always use cls for the first argument to class methods.
    @classmethod
    def make_friend(cls, current_user, new_friend): 
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend): 
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)