from django.db import models

from vote.models import VoteModel
from django_comments.abstracts import CommentAbstractModel
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill



class KitPost(VoteModel, models.Model): 
    #might need to fix the html view 
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)
    image = ProcessedImageField(upload_to='cover_photo',
                                           processors=[ResizeToFill(500, 500)],
                                           format='JPEG',
                                           options={'quality': 100})
    category = models.ForeignKey('category.Category', null=True, blank=True,default=None, on_delete=models.CASCADE)
    #This private_category refers to the User that owns the category
    private_category = models.ForeignKey('category.Private_Category', null=True, blank=True, default=None, on_delete=models.CASCADE)
    #This private_category2 refers to the Users that joined the private category.
    private_category2 = models.ForeignKey('category.Private_Users', null=True, blank=True, default=None, on_delete=models.CASCADE)

    class Meta: 
        ordering = ['-vote_score']
    

def get_image_filename(instance, filename): 
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)

class Images(models.Model): 
    post = models.ForeignKey(KitPost, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='test_file',
        )
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)
    product_url = models.CharField(max_length=150)



#model testing the comment function.
class testcomment(VoteModel, models.Model): 
    
    name = models.CharField(max_length = 150)
    
    
class CommentWithTitle(VoteModel, CommentAbstractModel): 
    
    title = models.CharField(max_length = 200) 
    
    
    def get_comment_create_data(self): 
        # Use the data of the superclass, and add in the title field
        
        data = super(CommentWithTitle, self).get_comment_create_data()
        data['title'] = self.cleaned_data['title'] 
        return data

    class Meta: 
        ordering = ['-vote_score']

    """ Not sure how to use this but it might work sometime later if I figure it out
    @property
    def sorted_comment_set(self):
        return self.CommentWithTitle.order_by('submit_date')
        """


