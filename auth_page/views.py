from django.shortcuts import render, redirect
from homepage.models import Album, Menu
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):

    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('auth_page:login')

    else:
        return render(request, 'auth_page/log_in.html')

def sign_up(request):

    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        conf_pass = request.POST['pass']

        if password == conf_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User name already exist!")
                return redirect('auth_page:sign_up')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist!")
                return redirect('auth_page:sign_up')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password,
                )
                user.save()
                messages.info(request, "Your account created!")
                return redirect('auth_page:login')
        else:
            messages.info(request, "Passwords do not match!")
            return redirect('auth_page:sign_up')
        
    else:
        return render(request, 'auth_page/sign_up.html')

def logout(request):
    auth.logout(request)
    return redirect("/")