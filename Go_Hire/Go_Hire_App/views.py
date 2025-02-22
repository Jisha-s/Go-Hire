from django.shortcuts import render,redirect

from .models import UserRegistration
from . forms import UserRegistrationForm
from django.contrib import messages
# Home page
def HomePage(request):
    return render(request, 'HomePage.html')

# creating user account
def CreateUserAccount (request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LoginUser')
    context={
            'form': form
    }
    return render(request, 'CreateUserAccount.html',context)

# Login for user
def LoginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = UserRegistration.objects.get(email=email, password=password)
        if user:
            return redirect('/Go-Hire')
        else:
            return redirect('Loginuser')
    return render(request, 'LoginUser.html')


def ForgotPassword(request):
    reset_password = False
    email = request.POST.get('email')

    if request.method == 'POST':
        email = request.POST.get('email')
        user = UserRegistration.objects.filter(email=email)
        if user:
            reset_password = True
        else:
            messages.error(request,"Email Not Found!!")
    context={
        'reset_password': reset_password,
        'email':email
    }
    return render(request, 'ForgotPassword.html',context)
    
def UpdatePassword(request):
    if request.method == 'POST':
        
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            try:
                user = UserRegistration.objects.get(email=email)
                user.password = confirm_password
                user.save()
                messages.success(request,'Your password has been updated successfully.')
                return redirect('LoginUser')
            except UserRegistration.DoesNotExist: 
                messages.error(request,'User does not exist')
        else:
            messages.error(request,'Password does not match')
        
 
    return render(request, 'ForgotPassword.html')
