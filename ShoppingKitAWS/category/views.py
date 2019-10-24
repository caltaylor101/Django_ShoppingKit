from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import CategoryForm, PrivateCategoryForm
from .models import Category, Private_Category, Private_Users
from django.shortcuts import get_object_or_404
from kit.models import KitPost
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def create_category(request):
    if request.method == 'POST': 
        categoryForm = CategoryForm(
            request.POST,
            request.FILES,
            )
        
        if categoryForm.is_valid(): 
            category_form = categoryForm.save(commit=False)
            category_form.user = request.user
            category_form.save()

            
            #redirect with parameter currently does nothing.
            #base_url = reverse('create-kit:viewkit')
            #url = '{}{}'.format(base_url, post_form.pk)
            
            return redirect(reverse('create-kit:create-kit'))
        else: 
            print(categoryForm.errors)
    else: 
        categoryForm = CategoryForm()

        return render(
            request,
            'category/create_category.html',
            {'categoryForm': categoryForm}
        )


#Still working on this view, just a copy of createCategory right now
@login_required
def create_private_category(request): 
    if request.method == 'POST': 
        privateCategoryForm = PrivateCategoryForm(
            request.POST,
            request.FILES,
            )
        
        if privateCategoryForm.is_valid(): 
            privateCategoryForm.owner = request.user
            private_category_form = privateCategoryForm.save(commit=False)
            private_category_form.owner = request.user
            
            

            
            
            private_category_form.save()

            
            #redirect with parameter currently does nothing.
            #base_url = reverse('create-kit:viewkit')
            #url = '{}{}'.format(base_url, post_form.pk)
            
            return redirect(reverse('create-kit:create-kit'))
        else: 
            formerrors = privateCategoryForm.errors
            return render(
            request,
            'category/create_private_category.html',
            {'privateCategoryForm': privateCategoryForm, 'formerrors':formerrors})
    else: 
        privateCategoryForm = PrivateCategoryForm()

        return render(
            request,
            'category/create_private_category.html',
            {'privateCategoryForm': privateCategoryForm},
            
        )

#this isn't working yet.
def get_redirected(queryset_or_class, lookups, validators):
    """
    Calls get_object_or_404 and conditionally builds redirect URL
    """
    obj = get_object_or_404(queryset_or_class, **lookups)
    for key, value in validators.items():
        if value != getattr(obj, key):
            return obj, obj.get_absolute_url()
    return obj, None



def category_view(request, pk):
    pk = pk
    category = Category.objects.get(id = pk)
    post = KitPost.objects.filter(category=pk)
    

    return render(
        request,
        'category/category_view.html',
        {'category':category, 'post':post, 'pk':pk,}
    )
@login_required
def private_category_view(request, pk): 

    category = Private_Category.objects.get(id = pk)
    
    authlist = Private_Users.objects.filter(category__id = pk)
    authpost = KitPost.objects.filter(private_category2__category__id = pk)
    post = KitPost.objects.filter(private_category = pk) | authpost
    users = User.objects.exclude(id=request.user.id)
    #This is a temporary solution for user authentication to the private category
    #It should be revised.
    
    if request.user == category.owner: 
        
        return render(
            request, 
            'category/private_category_view.html',
            {'category':category, 'post':post, 'authlist':authlist, 'users':users, 'pk':pk},
            
        )
    elif Private_Users.objects.filter(name = request.user, category=category).exists(): 


        return render(
            request, 
            'category/private_category_view.html',
            {'category':category, 'post':post, 'authlist':authlist, 'users':users, 'pk':pk},
            
        )

        

    else:
        
        base_url = reverse('category:private_category_login_no_pk')
        
        url = '{}{}'.format(base_url, pk)
        #eventually redirect to the post page. 
        return redirect(url)
        
@login_required
def private_category_login(request, pk = None): 
    #view is always a GET request. No else needed.
    if request.method == "GET": 
        
        query = request.GET.get('q')
        
        category_password = Private_Category.objects.get(id=pk).category_password
        
        private_category = Private_Category.objects.get(id=pk)
        
        
        if query == category_password: 
            
            user = request.user.username
            
            category = Private_Users.objects.create(name=user, category=private_category)
            base_url = reverse('category:private_category_view_no_pk')
            
            
            url = '{}{}'.format(base_url, pk)
            #eventually redirect to the post page. 
            return redirect(url)
    
        else: 
            return render(request, 'category/private_category_login.html', {'private_category':private_category})
        


    


def browse_categories(request): 

    categories = Category.objects.all()

    return render(
        request,
        'category/browse_categories.html',
        {'categories':categories}
    )


def join_private_category(request): 
    
    
   
    if request.method == "GET": 
        searchquery = request.GET.get('q')

        if searchquery:
           
            searchquery = Private_Category.objects.filter(title = searchquery)
        else:
            searchquery = None


        return render(
            request, 
            'category/join_private_category.html', 
            {
                'searchquery':searchquery,
            }
            )

    else: 

        return render(
                request, 
                'category/join_pivate_category.html', 
                {'searchquery':searchquery}
                
                )
