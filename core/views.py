from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal
from account.models import User

from .models import Tenor, Commodity, Dashboard, Withdraw, Crypto, WithdrawBank, Deposit, Items


def home(request):
    """Displays the index page."""
    template_name = 'index.html'
    return render(request, template_name)

@login_required
def dashboard(request):
    """Displays the index page."""
    template_name = 'dashboard.html'
    user = request.user
    dashboards = Dashboard.objects.get_or_create(user=user)
    context = {'dashboards': dashboards} 

    if request.method == 'POST':
        new_password = request.POST['new_password']
        u= User.objects.get(user=user)
        u.set_password(new_password)
        u.save()
        redirect('core:dashboard')
    return render(request, template_name, context)

@login_required
def portfolio(request):
    """Displays the index page."""
    template_name = 'portfolio.html'
    user = request.user
    dashboards = Dashboard.objects.get_or_create(user=user)
    dashboard = Dashboard.objects.filter(user=user,)
    available_balance = Decimal(Dashboard.objects.get(user=user,).profile_value)
    if request.method == 'POST':
        account_name = request.POST['account_name']
        account_number = request.POST['account_number']
        amount = request.POST['amount']
        swift = request.POST['swift']
        bank_name = request.POST['bank_name']
        bank_address = request.POST['bank_address']
        bank_state = request.POST['bank_state']
        bank_zip_code  = request.POST['bank_zip_code']
        bank_country = request.POST['bank_country']
        additional_instructions = request.POST['additional_instructions']

        new_amount = Decimal(amount)
        if new_amount > available_balance:
            messages.info(request, "Insufficient Wallet Balance! Please fund your Wallet.")
            return redirect('core:portfolio')
        
        available_balance -=new_amount
        dashboard.update(profile_value=available_balance)
        withdraws = Withdraw(name=account_name, account=account_number, amount=amount, swift=swift, bank_name=bank_name, bank_address=bank_address,
                         bank_state=bank_state, bank_zip_code=bank_zip_code, bank_country=bank_country, additional_instructions=additional_instructions)
        withdraws.user = user
        withdraws.save()
        messages.info(request, 'Processing...Transaction processing!')

    context = {'dashboards': dashboards} 
    return render(request, template_name, context)

@login_required
def change_password(request):
    user = request.user
    u= User.objects.get(user=user)
    u.set_password()
    u.save()

def assets(request):
    """Displays the index page."""
    template_name = 'assets.html'
    return render(request, template_name)

def deposit(request):
    """Displays the index page."""
    template_name = 'deposit.html'
    cryptos = Crypto.objects.all()
    context = {'cryptos': cryptos}
    return render(request, template_name, context)

def about(request):
    """Displays the index page."""
    template_name = 'about.html'
    return render(request, template_name)