# -*- encoding: utf-8 -*-
from django.shortcuts import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect


from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext

# envio de mail
from django.core.mail import EmailMessage

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from factu.models import Usuario
from django.http import JsonResponse
from django.core import serializers

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time

from django.contrib.auth.models import User





HTML = """
<html>
<h1>Usuarios Creados!!!...</h1>
</html> """

def hola(request):
    return HttpResponse(HTML)

def login(request):
    return render(request, 'login.html')

def auth_view(request):

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		if user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect('/home/')
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

@login_required(login_url='/auth_view')
def home(request):
	return render_to_response('home.html', {'user': request.user}, context_instance=RequestContext(request))

@login_required(login_url='/auth_view')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


@login_required(login_url='/auth_view')
def estudiantesIndex(request):
    usuarios = Usuario.objects.all()
    paginator = Paginator(usuarios, 15)

    page = request.GET.get('page')

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'usuarios.html', {'usuarios':users})

@login_required(login_url='/auth_view')
def llenaUsuarios(request):
    for i in range(1,40):
            usuario = "dav%s"%i
            contrasenia = "banda%s"%i
            nombre = "david%s"%i
            apellidos = "david%s"%i
            matricula = i
            telefono = "222015%s"%i
            ci = "70247%s"%i
            tipo_usuario = 1
            usuario = Usuario(
            usuario=usuario,
            contrasenia=contrasenia,
            nombre=nombre,
            apellidos=apellidos,
            matricula=matricula,
            telefono=telefono,
            ci = ci,
            tipo_usuario=tipo_usuario)
            usuario.save()
    return HttpResponse(HTML)

@login_required(login_url='/auth_view')
def estudiantesIndexJson(request):
    usuarios = Usuario.objects.filter()
    for user in usuarios:
        response = JsonResponse(usuarios, safe=False)
    return response


@login_required(login_url='/auth_view')
def buscarEstudiante(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            return redirect('/estudiantesIndex/')
        else:
            estudiante = Usuario.objects.filter(id__icontains=q) or Usuario.objects.filter(nombre__icontains=q) or Usuario.objects.filter(apellidos__icontains=q) or Usuario.object.filter(matricula__icontains=q) or Usuario.object.filter(telefono__icontains=q) or Usuario.object.filter(email__icontains=q)
            paginator = Paginator(estudiante, 15)
            page = request.GET.get('page')
            try:
                users = paginator.page(page)
            except PageNotAnInteger:
                users = paginator.page(1)
            except EmptyPage:
                users = paginator.page(paginator.num_pages)
            return render(request, 'usuarios.html', {'usuarios':users, 'query':q})
	return render(request, 'buscar_autor.html', {'errors':errors})

#ACCOUNT
def crear(request):
    return render(request, "register.html")

def register_account(request):
    if request.method == 'POST':
        # return HttpResponse('<h1>es metodo post</h1>')
        usuario = request.POST['username']
        contrasenia = request.POST['password']
        nombre = request.POST['firstname']
        apellido = request.POST['lastname']
        correo = request.POST['email']
        # fecha = time.strftime("%y/%m/%d %H:%M:%S")
        account = User.objects.create_user(usuario, correo, contrasenia)
        account.first_name = nombre,
        account.last_name = apellido
        account.save()

        return HttpResponse('<h1>usuario Creado Correctamente</h1>')

# def register_account(request):
#     user = User.objects.create_user('juan', 'juan@gmail.com', 'juan')
#     user.last_name = 'Perez'
#     user.first_name = 'Juanito'
#     user.telefono = 22211545
#     user.matricula = 8000961
#     user.ci = 7024740
#     user.save()
#     return HttpResponse('<h1>usuario Creado Correctamente</h1>')
