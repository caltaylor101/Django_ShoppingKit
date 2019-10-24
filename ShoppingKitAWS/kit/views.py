from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.forms import modelformset_factory

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ImageForm, PostForm
from .models import Images, KitPost, testcomment, CommentWithTitle
from django.urls import reverse
from django.views.generic import TemplateView
from django.template import RequestContext
from urllib.parse import urlencode
from kit.forms import CommentFormWithTitle
from django.contrib.auth.models import User

from django.views.decorators.http import require_POST
from django.template.defaultfilters import slugify
import json
from django.utils import timezone

from category.models import Category, Private_Users, Private_Category
from django.contrib.auth.decorators import login_required




#post is the create kit view
@login_required
def post(request): 



    user = request.user
    
    
    
    ImageFormSet = modelformset_factory(Images,form = ImageForm,extra= 10)
    #extra is the number of photos that can be uploaded
    
    #Form logic to submit a post with multiple images attached. 
    if request.method == 'POST': 
        
    
        #First post form that assigns the primary key
        #request current user for use in the private_category section of the form.
        postForm = PostForm(
            
            user,
            request.POST,
            request.FILES,
            
            
            
            )
        #Second form for multiple photos
        formset = ImageFormSet(
            request.POST, 
            request.FILES,
            queryset=Images.objects.none(),
            
            )
        
        
        
        #Checks validation in both forms. 
        if postForm.is_valid() and formset.is_valid(): 
            
            #commit is false so that we can request the user before saving it. 
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            
            #saves the first form. 
            post_form.save()

            #Cleaned_data allows us to access the data inside of our saved form.
            for form in formset.cleaned_data: 
                #this helps to not crash if the user
                #does not upload all the photos
                if form:
               
                    title= form.get('title')
                    body = form.get('body')
                    
                    image = form['image']
                    product_url = form['product_url']

                    
                    #Saves to post_form
                    photo = Images(post=post_form, title=title, body=body, image=image, product_url=product_url)
                    photo.save()
                    
            
            

            #redirect with parameter
            base_url = reverse('create-kit:viewkit')
            url = '{}{}'.format(base_url, post_form.pk)
            #eventually redirect to the post page. 
            return redirect(url)
        else: 
            
            print(postForm.errors, formset.errors)
    else: 
        
        postForm = PostForm(user = request.user)
        formset = ImageFormSet(queryset=Images.objects.none()) 

    
    return render(
        request,
        'kit/create-kit.html',
        {'postForm': postForm, 'formset':formset, 'user':user}
    )

    



#pk used to be pk=None on old code
def viewkit(request, pk): 
    
    #New Code
    user = request.user
    post = KitPost.objects.get(id=pk)
    album = Images.objects.filter(post_id = post)
    identifier = post.id

    
    
    #old working code
    """if pk:    
        post = KitPost.objects.get(id=pk)
        album = Images.objects.filter(post_id = post)

        
        return render(request, 'kit/viewkit.html', {'album':album, 'post':post})"""

    #testing timezones
    now = timezone.now()

    return render(request, 'kit/viewkit.html', {'album':album, 'post':post, 'identifier':identifier,'user':user, 'now':now})
    


#Comment test view
def testingcomments(request, id=None): 
    b = testcomment(name='Hello')
    b.save()
    
    
    
    if id:
        entry = testcomment.objects.get(id=id)
        test = entry.id
 
        

        return render(request, 'kit/test.html', {'entry':entry, 'test':test})

    else:
        return render(request, 'kit/test.html')



def upvote(request, id=None):
    user = request.user
    slug = request.POST.get('slug', None) 
    
    commenting = CommentWithTitle.objects.get(id=slug)
    
    if commenting.votes.exists(user.id): 
        commenting.votes.delete(user.id)
    else: 
        commenting.votes.up(user.id)

    #redirection doesn't work yet, trying to figure out how to get AJAX to be instant. 
    base_url = reverse('create-kit:viewkit')
    url = '{}{}'.format(base_url, commenting.content_object.id)
    #eventually redirect to the post page. 
    return redirect(url)


def downvote(request, id=None):
    user = request.user
    slug = request.POST.get('slug', None) 
    
    commenting = CommentWithTitle.objects.get(id=slug)
    
    if commenting.votes.exists(user.id): 
        commenting.votes.down(user.id)
        commenting.votes.down(user.id)
    else: 

    
        commenting.votes.down(user.id)
    
    

    base_url = reverse('create-kit:viewkit')
    url = '{}{}'.format(base_url, commenting.content_object.id)
    #eventually redirect to the post page. 
    return redirect(url)



def upvote_post(request, id=None):
    user = request.user
    slug = request.POST.get('slug', None) 
    
    kitpost = KitPost.objects.get(id=slug)
    
    if kitpost.votes.exists(user.id): 
        kitpost.votes.delete(user.id)
    else: 

    
        kitpost.votes.up(user.id)
    
    

    base_url = reverse('create-kit:viewkit')
    url = '{}{}'.format(base_url, kitpost.content_object.id)
    #eventually redirect to the post page. 
    return redirect(url)

def downvote_post(request, id=None):
    user = request.user
    slug = request.POST.get('slug', None) 
    
    kitpost = KitPost.objects.get(id=slug)
    
    if kitpost.votes.exists(user.id): 
        kitpost.votes.down(user.id)
        kitpost.votes.down(user.id)
    else: 

    
        kitpost.votes.down(user.id)
    
    

    base_url = reverse('create-kit:viewkit')
    url = '{}{}'.format(base_url, kitpost.content_object.id)
    #eventually redirect to the post page. 
    return redirect(url)



    
def sort_comments(request, id=None):
    
    slug = request.POST.get('slug', None) 
    
    commenting = CommentWithTitle.objects.get(id=2)
    filter_id = commenting.content_type.id
    
    if slug == 'newest': 
        CommentWithTitle.objects.filter(content_type = 12).order_by('submit_date')
    
    

    base_url = reverse('create-kit:viewkit')
    url = '{}{}'.format(base_url, commenting.content_object.id)
    #eventually redirect to the post page. 
    return redirect(url)

    
    



    


