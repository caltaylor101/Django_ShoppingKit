from django import forms
from .models import Category, Private_Category


from django.core.exceptions import ValidationError


class PrivateCategoryForm(forms.ModelForm): 
    title = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control', 
            'style':'width:50%',
            'placeholder': 'Write a Title for Your Private Category', 
            'autocomplete':'off',
        }
    ), max_length=200, required = True)

    description = forms.CharField(widget=forms.TextInput(
        attrs= {
            'class':'form-control',
            'placeholder':'Write a Description for Your Category'
        }
    ),max_length = 500, required=False, label="Category Description.")

    image = forms.ImageField(label='Image') 

    category_password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
        'autocomplete':'off',
        'placeholder':'password',
        }
    ))

    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'autocomplete':'off',
            'placeholder':'retype password'
        }
    ))

    
    class Meta:
        model = Private_Category
        widgets = {
        'category_password': forms.PasswordInput(),
    }
        fields = ('title', 'description', 'category_password','confirm_password', 'image', )

    #Checks to make sure that the passwords are the same
    
    def clean(self):
        cleaned_data = super(PrivateCategoryForm, self).clean()
        category_password = cleaned_data.get('category_password')
        confirm_password = cleaned_data.get('confirm_password')

        if category_password != confirm_password:
            raise forms.ValidationError(
                    "The passwords don't match"
                )
    
    """
    def clean(self):
        
        cleaned_data = super(PrivateCategoryForm, self).clean()
        category_password = cleaned_data.get("category_password")
        confirm_password = cleaned_data.get("confirm_password")

        if category_password != confirm_password:
            
            cc_myself = self.cleaned_data.get("cc_myself")
"""





class CategoryForm(forms.ModelForm): 
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'style':'width:50%',
            'placeholder':'Write a Title for Your Category'
        }
    ), max_length=120, required=True)

    description = forms.CharField(widget=forms.TextInput(
        attrs= {
            'class':'form-control',
            'placeholder':'Write a Description for Your Category'
        }
    ),max_length = 500, required=False, label="Category Description.") 

    
    image = forms.ImageField(label='Image')
    
    

    class Meta: 
        model = Category
        fields = ('name', 'description', 'image',) 

