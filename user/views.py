from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

def pagina_login(request):
    # Se já estiver logado, redireciona para home
    if request.user.is_authenticated:
        return redirect('police_car:home')
    
    if request.method == 'POST':
        email = request.POST.get('email')  # Agora usa email
        password = request.POST.get('password')
        
        # Autentica com email
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.first_name}!')
            return redirect('police_car:home')
        else:
            messages.error(request, 'Email ou senha incorretos.')
    
    return render(request, 'user/login.html')

def pagina_cadastro(request):
    if request.user.is_authenticated:
        return redirect('police_car:home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        # Verifica se o email já existe
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este email já está cadastrado.')
        else:
            # Cria o usuário
            user = Usuario.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            login(request, user)
            messages.success(request, f'Cadastro realizado com sucesso! Bem-vindo, {user.first_name}!')
            return redirect('police_car:home')
    
    return render(request, 'user/register.html')

def fazer_logout(request):
    logout(request)
    return redirect('user:login')