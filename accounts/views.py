from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProfileForm
from .models import Profile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        u_form = UserRegistrationForm(request.POST)
        p_form = ProfileForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            user.set_password(u_form.cleaned_data['password'])
            user.save()

            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('home')
    else:
        u_form = UserRegistrationForm()
        p_form = ProfileForm()

    return render(request, 'accounts/register.html', {'u_form': u_form, 'p_form': p_form})

@login_required
def profile_view(request):
    # Ensure a Profile exists for the user (create default if missing)
    profile, created = Profile.objects.get_or_create(user=request.user, defaults={'bio': ''})
    posts = getattr(request.user, 'blog_set', []).all() if hasattr(request.user, 'blog_set') else []
    return render(request, 'accounts/profile.html', {'profile': profile, 'posts': posts})


def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        next_url = request.POST.get('next') or request.GET.get('next') or 'home'

        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            error = 'Invalid Username or Password!'

    next_param = request.GET.get('next', '')

    return render(request, 'accounts/login.html', {'error': error, 'next':next_param})
        

# --------------Log-Out

def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login_view')

    else:
        return redirect('home')




