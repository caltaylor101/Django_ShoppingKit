from django import forms
from django_comments.forms import CommentForm
from kit.models import CommentWithTitle
from .models import KitPost, Images
from category.models import Category, Private_Category, Private_Users

from django.forms import ModelChoiceField, Form


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.category


class PostForm(forms.ModelForm): 

    category= forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(
        attrs={
            'style' : 'width:33%; '
        }
    ), required=False)

    private_category = forms.ModelChoiceField(queryset = None, widget=forms.Select(
        attrs={
            'style':'width:33%;'

    }), required=False)


   
    private_category2 = MyModelChoiceField(queryset = None, widget=forms.Select(
        attrs={
            'style':'width:33%;'

    }), required=False) 
    

    #This allows us to use request.user from our view. 
    #It replaces the queryset in the private_category above. 
    
    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['private_category'].queryset = Private_Category.objects.all().filter(owner=user)
        self.fields['private_category2'].queryset = Private_Users.objects.all().filter(name=user)
        


    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'style':'width:50%',
            'placeholder':'Write a Title for Your Post'
        }
    ), max_length=120, required=False)
    body = forms.CharField(widget=forms.TextInput(
        attrs= {
            'class':'form-control',
            'placeholder':'Write a Description for Your Post'
        }
    ),max_length = 500, required=False, label="Item Description.") 

    
    image = forms.ImageField(label='Image')

  
        
    
    
    
    
    
    

    class Meta: 
        model = KitPost
        fields = ('title', 'body', 'image','category', 'private_category', 'private_category2') 

class ImageForm(forms.ModelForm): 
    title = forms.CharField(label='', max_length=128, required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'style':'width:50%; margin-top:15px',
            'placeholder':'Write a Title for the Product'
        }
    ))
    body = forms.CharField(label='', max_length=245, required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'style': 'margin-top:15px;margin-bottom:15px',
            'placeholder':'Write a Description for the Product'
        }
    ))
    image = forms.ImageField(label='') 
    class Meta: 
        model = Images
        fields = (
        
        'image',
        'title',
        'body',
        )

    product_url = forms.CharField(label='', max_length=150, required=False, widget=forms.TextInput(
        attrs={ 
            'class': 'form-control', 
            'style': 'margin-top:15px;margin-top:15px',
            'placeholder':'Enter the url for the product here'

        }
    ))

    
class CommentFormWithTitle(CommentForm): 
    title = forms.CharField(max_length=150, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Title for Comment',
            'style': 'width:30%;'
        }
    ))

    comment = forms.CharField(max_length=500, required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comment here...',
            
        }
    ))
        
    
    def get_comment_create_data(self, **kwargs): 
        # Use the data of the superclass, and add in the title field
        data = super(CommentFormWithTitle, self).get_comment_create_data()
        data['title'] = self.cleaned_data['title']
        data['comment'] = self.cleaned_data['comment']
        
        return data



"""    
class CategoryForm(forms.ModelForm): 

   
    category = forms.ModelChoiceField(queryset=Category.objects.values_list('name',flat=True))


    

    # select names with:
    # values_list('name',flat=True)
    # this shouldn't be used with the model above
    
   
    
    
    

    class Meta: 
        model = Category
        fields = ['category',]

"""
