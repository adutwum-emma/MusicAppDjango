from django.shortcuts import render, render, get_object_or_404, redirect
from django.contrib.auth.models import auth, User
from django.http import HttpResponse
from django.contrib import messages
from homepage.models import Album
from django.contrib.auth import hashers

def profile(request, user_id):

    user = User.objects.get(pk=user_id)

    return render(request, "account/profile.html", {'user':user})

def editProfile(request, user_id):
    if request.method == 'POST':
        new = request.POST['use']
        user = get_object_or_404(User, pk=new)
        try:
            username = request.POST['username']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email']
        except (KeyError, User.DoesNotExist):
            messages.info(request, "Fill in the required fields")
            return redirect('/account/' + str(user_id) + '/' + 'editProfile')
        else:
            new = request.POST['use']

            if new == user_id:
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                return redirect('/account/'+ str(user_id))
            else:
                return redirect("/")
    else:
        user = User.objects.get(pk=user_id)

        if User is None and user.id == user_id:
            return redirect("/")
        else:
            return render(request, "account/editProfile.html", {'user':user})
            
        #user = User.objects.get(pk=user_id)
        

def delete(request):
    user_id = request.POST['user_id']
    try:
        album = get_object_or_404(Album, pk=request.POST['album'])
    except (KeyError):
        messages.info(request, "You did not select any album!")
        return redirect('/account/' + str(user_id))
    else:
        if user_id == "":
            return redirect('/account/' + str(user_id))
        else:
            album.delete()
            return redirect('/account/' + str(user_id))

def changePass(request, user_id):


    if request.method == 'POST':
        user = request.POST['the_id']
        my_pass = User.objects.get(pk=user)
        old = request.POST['oldPass']
        new  = request.POST['newPass']
        con = request.POST['conPass']
        

        my_check = hashers.check_password(old, my_pass.password) 

        if my_check == True:
            if my_pass.id == user_id:
                if new  == con:
                    my_pass.set_password(new)
                    my_pass.save()
                    messages.info(request, "Password changed")
                    return redirect('/account/' + str(user_id) + '/changePass/')
                else:
                    messages.info(request, "Passwords do not match")
                    return redirect('/account/' + str(user_id) + '/changePass/')
            else:
                return redirect("/")
        else:
            messages.info(request, "Wrong password")
            return redirect('/account/' + str(user_id) + '/changePass/')
                
    else:
        return render(request, "account/changePass.html")
    
    