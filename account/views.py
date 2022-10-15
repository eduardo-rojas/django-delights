from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login 
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import Profile



@login_required
def dashboard(request):
    username = request.user.id
    current_user = Profile.objects.get(user_id=username)
    return render(request, 
                    'account/dashboard.html',
                    {'section': 'dashboard',
                    'current_user': current_user})