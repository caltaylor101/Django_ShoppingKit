from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm, 
    PasswordChangeForm
)

from django.contrib.auth import (
    logout, 
    authenticate, 
    login,
    update_session_auth_hash
)

from accounts.forms import (
    RegistrationForm, 
    EditProfileForm 
    
)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.

def register(request): 
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect(reverse('home:homepage'))
        
    else: 
        form = RegistrationForm()
        
        args = {'form': form} 
        return render(request, 'accounts/reg_form.html', args)
    
    form = RegistrationForm
    return render(
        request = request, 
        template_name = "accounts/reg_form.html",
        context={'form':form}
    )

@login_required
def view_profile(request, pk=None): 
    if pk: 
        user = User.objects.get(pk=pk)
    else: 
        user = request.user

    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request): 
    if request.method == 'POST': 
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid(): 
            form.save()
            return redirect('/accounts/profile')

    else: 
        form = EditProfileForm(instance=request.user) 
        args = {'form': form} 
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == "POST": 
        form = PasswordChangeForm(data=request.POST, user = request.user)
        if form.is_valid(): 
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')

        else:
            return redirect('/accounts/change-password')
        
    else: 
        form = PasswordChangeForm(user = request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)



