
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth
from .models import User
    
def registration(request):
    """Displays the index page."""
    template_name = 'signup.html'
    if request.method == 'POST':
        first_name = request.POST['first_name']
        surname = request.POST['surname']
        email = request.POST['email']
        phone = request.POST['phone']
        date_of_birth = request.POST['date_of_birth']
        address = request.POST['address']
        postal_code  = request.POST['postal_code']
        stage = request.POST.get("security_answer", "None")
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'email already exist.')
            return redirect('account:registration')
        if password == confirm_password:
            user = User.objects.create_user(first_name=first_name, surname=surname, dob=date_of_birth, email=email, phone=phone, address=address, postal_code=postal_code, stage=stage, password=password)
            user.save()
            return redirect('account:login')
        messages.info(request, 'Password does not match!.')
        return redirect('account:registration')
    return render(request, template_name)

def login(request):
    """Displays the index page."""
    template_name = 'login.html'
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('core:dashboard')
        messages.info(request, 'Invalid Credentials.')
        return redirect('account:login')
    return render(request, template_name)

def logout(request):
    """Returns the logout page, redirecting to the home page."""
    auth.logout(request)
    return redirect('core:home')

 