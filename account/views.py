from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, UpdateUserForm, ProfileUpdateForm

from django.contrib.sites.shortcuts import get_current_site
from .token import user_tokenizer_generate

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import User

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings


def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            
            # Email verification setup (template)
            
            current_site = get_current_site(request)
            subject = 'Account verification email'
            message = render_to_string('account/registration/email-verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user),
            })
            
            
            user.email_user(subject=subject, message=message)
            
            return redirect('email-verification-sent')
            
            
    context = {
        'form': form,
        'title': 'Register'
    }
    return render(request, 'account/registration/register.html', context)

def email_verification(request, uidb64, token):
    unique_id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=unique_id)
    
    # Success
    
    if user and user_tokenizer_generate.check_token(user, token):
        #uniqueid
        user.is_active = True
        user.save()
        return redirect('email-verification-success')
    
    # Failed
    else:
        return redirect('email-verification-failed')
    
    

def email_verification_sent(request):
    
    context = {
        'title': ''
    }
    return render(request, 'account/registration/email-verification-sent.html', context)

def email_verification_success(request):
    
    context = {
        'title': ''
    }
    return render(request, 'account/registration/email-verification-success.html', context)

def email_verification_failed(request):
    
    context = {
        'title': ''
    }
    return render(request, 'account/registration/email-verification-failed.html', context)

def my_login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('index')
    context = {
        'form': form,
        'title': 'Login'
    }
    return render(request, 'account/my-login.html', context)

def user_logout(request):
    auth.logout(request)
    
    return redirect('index')


@login_required(login_url='my-login')
def profile(request):
    
    # Update users
    
    u_form = UpdateUserForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('index')
        
    u_form = UpdateUserForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'account/profile.html', context)


@login_required(login_url='my-login')
def delete_account(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.delete()
        return redirect('index')
    return render(request, 'account/delete-account.html')