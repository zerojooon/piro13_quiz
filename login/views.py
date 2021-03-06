from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def social_login(request):
    return render(request, 'login/social_login.html')


def general_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('quiz:main')
        else:
            return render(request, 'login/social_login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login/social_login.html')


def sign_up(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('quiz:main')
        return render(request, 'login/signup.html')
    else:
        return render(request, 'login/signup.html')


def logout(request):
    auth.logout(request)
    return redirect('quiz:main')  # change to main page
