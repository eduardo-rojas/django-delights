from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login 
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile


# View for Home page
@login_required
def dashboard(request):
    # username = request.user.id
    # current_user = Profile.objects.get(user_id=username)
    return render(request, 
                    'account/dashboard.html',
                    {'section': 'dashboard'})
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
            return render(request, 
                            'account/register_done.html',
                            {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 
                    'account/register.html',
                    {'user_form': user_form})