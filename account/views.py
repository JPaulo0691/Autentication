from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Login Registrado')
                    
                else:
                    return HttpResponse('Conta Desconectada')
            else:
                return HttpResponse("Login inválido")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form' : form})

# We create a new view to display a screen control when users will doing login in their accounts.

# The login_required verifies if the user is authenticated. If the user was authenticated the login_required will be executed, if he isn't authenticated, the user will be redirected to url login.
@login_required

def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
