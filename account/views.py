from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login 
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


# View for Home page
@login_required
def home(request):
    # username = request.user.id
    # current_user = Profile.objects.get(user_id=username)
    return render(request, 
                    'account/home.html',
                    {'section': 'Home'})
                    #'current_user': current_user

# View to Register new account
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object
            new_user = user_form.save(commit=False)
            # Set password
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            # Save user object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 
                            'account/register_done.html',
                            {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 
                    'account/register.html',
                    {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                        data=request.POST,
                                        files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else: 
            messages.error(request, 'Error. Could not update your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                    'account/edit.html',
                    {'user_form': user_form,
                    'profile_form': profile_form})
