import email
from django.shortcuts import redirect, render
from logins.models import Users

# Create your views here.
def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        uemail = request.POST['uemail']
        username = request.POST['username']
        passwrd = request.POST['passwrd']



        if request.POST['passwrd'] == request.POST['conpasswrd']:
            registeruser = Users.objects.create(username=username, firstname=fname,
            middlename=mname, lastname=lname, email=uemail, password = passwrd)
            registeruser.save()
            return redirect('login')

    return render(request, 'registration/register.html')