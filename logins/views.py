from django.shortcuts import redirect, render
from .models import Users

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwrd = request.POST['passwrd']
        authuser = Users.objects.filter(username=username, password = passwrd)
        if authuser.exists():
            return #redirect('') redirect to the homepage here
        else:
            return render(request, 'login/login.html', {'msg': 'Login Failed'})
    return render(request, 'login/login.html')