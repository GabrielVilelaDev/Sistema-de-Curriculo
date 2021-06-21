from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Candidato, Contatos,  Habilidades, Objetivos, Formacao
from .forms import CandidatoForms, ContatoForms, HabilidadeForms, ObjetivosForms, FormacaoForms
from django.forms import modelformset_factory

# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    return redirect('do_login')

def home(request):
    return render(request, 'home.html')

def candidato(request):
    if request.user.is_authenticated:
        id = request.user.id
        candidato = Candidato.objects.filter(user=id).get()
        habilidades = Habilidades.objects.all().filter(candidato=candidato)
        objetivos = Objetivos.objects.all().filter(candidato=candidato)
        contatos = Contatos.objects.filter(candidato=candidato).get()
        formacoes = Formacao.objects.all().filter(candidato=candidato)
        dados = {
            'candidato': candidato,
            'contato': contatos,
            'objetivos': objetivos,
            'habilidades': habilidades,
            'formacao': formacoes,
        }
        return render(request, 'candidato.html', dados)
    return redirect('do_login/')

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
        id = request.user
        candidato_form_save = CandidatoForms(request.POST)
        contato_form_save = ContatoForms(request.POST)
        habilidades_form_save = HabilidadeForms(request.POST)
        objetivos_form_save = ObjetivosForms(request.POST)
        formacoes_form_save = FormacaoForms(request.POST)

        if candidato_form_save.is_valid() and contato_form_save.is_valid() and habilidades_form_save.is_valid() and objetivos_form_save.is_valid() and formacoes_form_save.is_valid():
            name = candidato_form_save.cleaned_data['name']
            foto = candidato_form_save.cleaned_data['foto_candidato']
            perfil = candidato_form_save.cleaned_data['perfil']
            resumo = candidato_form_save.cleaned_data['resumo']
            candidato = Candidato.objects.create(user=id, name=name, perfil=perfil, resumo=resumo, foto_candidato=foto)
            candidato.save()

            celular = contato_form_save.cleaned_data['celular']
            email = contato_form_save.cleaned_data['email']
            linkedin = contato_form_save.cleaned_data['linkedin']
            site = contato_form_save.cleaned_data['site']
            contatos = Contatos.objects.create(candidato=candidato, email=email, site=site, linkedin=linkedin, celular=celular)
            contatos.save()

            descricaoobj = objetivos_form_save.cleaned_data['descricaoobj']
            objetivos = Objetivos.objects.create(descricaoobj=descricaoobj, candidato=candidato)
            objetivos.save()

            descricaofor = formacoes_form_save.cleaned_data['descricaofor']
            formacao_object = Formacao.objects.create(descricaofor=descricaofor,candidato=candidato)
            formacao_object.save()

            descricaohab = habilidades_form_save.cleaned_data['descricaohab']
            habilidade_object = Habilidades.objects.create(descricaohab=descricaohab, candidato=candidato)
            habilidade_object.save()

        return redirect('dashboard')

    candidato_form = CandidatoForms()
    contato_form = ContatoForms()
    habilidades_form = HabilidadeForms()
    objetivos_form = ObjetivosForms()
    formacao_form = FormacaoForms()
    contexto = {'candidato_form': candidato_form, 'contato_form': contato_form,'habilidades_form':habilidades_form, 'objetivos_form':objetivos_form, 'formacao_form': formacao_form}
    return render(request, 'cadastro_curriculo.html', contexto)

def recrutador(request):
    if request.POST:
        nomedocandidato = request.POST['nome_candidato']
        candidato = Candidato.objects.filter(name=nomedocandidato).get()
        habilidades = Habilidades.objects.all().filter(candidato=candidato)
        objetivos = Objetivos.objects.all().filter(candidato=candidato)
        contatos = Contatos.objects.filter(candidato=candidato).get()
        formacoes = Formacao.objects.all().filter(candidato=candidato)
        dados = {
            'candidato': candidato,
            'contato': contatos,
            'objetivos': objetivos,
            'habilidades': habilidades,
            'formacao': formacoes,
        }
        return render(request, 'recrutador_candidato.html', dados)
    candidato = Candidato.objects.order_by('-name')
    contatos = Contatos.objects.order_by('celular')
    dados = {
            'candidato': candidato,
            'contato': contatos,
    }
    return render(request, 'recrutador.html', dados)

def recrutador_candidato(request, nomedocandidato):
    candidato = Candidato.objects.filter(name=nomedocandidato).get()
    habilidades = Habilidades.objects.all().filter(candidato=candidato)
    objetivos = Objetivos.objects.all().filter(candidato=candidato)
    contatos = Contatos.objects.filter(candidato=candidato).get()
    formacoes = Formacao.objects.all().filter(candidato=candidato)
    dados = {
            'candidato': candidato,
            'contato': contatos,
            'objetivos': objetivos,
            'habilidades': habilidades,
            'formacao': formacoes,
    }
    return render(request, 'candidato.html', dados)
    return redirect('do_login/')


