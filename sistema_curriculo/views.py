from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Candidato, Contatos,  Habilidades, Objetivos, Formacao
# Create your views here.

@login_required(login_url='do_login/')
def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'home.html')

def candidato(request):
    return render(request, 'candidato.html')

@csrf_protect
def do_login(request):
    if request.POST:
        username = request.POST.get('login')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user is not None:
            login(request, user)
            id = request.user.id
            if not Candidato.objects.order_by('name').filter(user=id).exists():
                return redirect('cadastro_curriculo')
            else:
                return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
    return render(request,'login.html')

def do_logout_user(request):
    logout(request)
    return redirect('/do_login/')

def cadastrar(request):
    if request.POST:
        nome = request.POST['nome']
        email = request.POST['email']
        param_login = request.POST['login']
        senha = request.POST['senha']
        if not nome.strip():
            messages.error(request, 'O campo nome não pode ficar em branco!')
            return redirect('cadastrar')

        if not email.strip():
            messages.error(request, 'O campo email não pode ficar em branco!')
            return redirect('cadastrar')

        if not param_login.strip():
            messages.error(request, 'O campo login não pode ficar em branco!')
            return redirect('cadastrar')

        if not senha.strip():
            messages.error(request, 'O campo senha não pode ficar em branco!')
            return redirect('cadastrar')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuario já existe!')
            return redirect('cadastrar')

        user = User.objects.create_user(username=param_login, email=email, password=senha, first_name=nome)
        user.save()
        return redirect('do_login')

    return render(request, 'cadastro.html')

def cadastro_curriculo(request):
    if request.POST:
        nome = request.POST['nome']
        foto = request.POST['foto']
        celular = request.POST['celular']
        email = request.POST['email']
        linkedin = request.POST['linkedin']
        site = request.POST['site']
        perfil = request.POST['perfil']
        Habilidades = request.POST['Habilidades']
        Objetivos = request.POST['Objetivos']
        resumo = request.POST['resumo']
        Formacao = request.POST['Formacao']

        print(nome, foto, celular, email, linkedin, site, perfil, Habilidades, Objetivos, resumo, Formacao)
        return redirect('dashboard')

    return render(request, 'cadastro_curriculo.html')