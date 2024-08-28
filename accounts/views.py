from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile

# Create your views here.

# Login 
def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found!')
            return HttpResponseRedirect(request.path_info)
        
        elif not user_obj[0].profile.is_email_verified:
            messages.warning('Your account is not verified! check your email for verification')
            return HttpResponseRedirect(request.path_info)

        else :
            user_obj = authenticate(
                request,
                username = email,
                password = password
            )

            if user_obj:
                login(request, user_obj)
                return redirect('')

    return render(request, 'accounts/login.html')



# Registeration
def registeraion_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # print(request.POST)
        user = User.objects.filter(email = email)

        if password != confirm_password:
            messages.warning(request, 'Password Missmatch!')
            return HttpResponseRedirect(request.path_info)
  
        elif user.exists():
            messages.warning(request, 'Email already exisit!')
            return HttpResponseRedirect(request.path_info)
        
        else:
            user_obj = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = email
            )
            user_obj.set_password(password)
            user_obj.save()
            
            messages.success(request, 'An verification mail hass been send to your email please check it out before login')
            return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/register.html')


# Activate acoount 
def activate_account(request, email_token):
    try:
        user = Profile.objects.get(email_token = email_token)
        user.is_email_verified =True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid email token')
