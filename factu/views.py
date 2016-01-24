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
    usuarios = User.objects.all()
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
    for i in range(10000,65000):
            usuario = "dav%s"%i
            contrasenia = "banda%s"%i
            nombre = "david%s"%i
            apellidos = "david%s"%i
            matricula = i
            telefono = "215%s"%i
            ci = "702%s"%i
            tipo_usuario = 1
            usuario = User(
            username=usuario,
            password=contrasenia,
            first_name=nombre,
            last_name=apellidos,
            matricula=matricula,
            ci = ci)
            usuario.save()
    return HttpResponse(HTML)

@login_required(login_url='/auth_view')
def estudiantesIndexJson(request):
    usuarios = User.objects.filter()
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
            estudiante = User.objects.filter(id__icontains=q) or User.objects.filter(first_name__icontains=q) or User.objects.filter(last_name__icontains=q) or User.object.filter(matricula__icontains=q) or User.object.filter(email__icontains=q)

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
    errors = []
    if request.method == 'POST':
        # return HttpResponse('<h1>es metodo post</h1>')
        if not request.POST.get('username', ''):
            errors.append('Por favor Introduce el Usuario')
        duplicado = User.objects.filter(username = request.POST.get('username'))
        if duplicado:
            errors.append('El Usuario ya Existe.')
        if not request.POST.get('password', ''):
            errors.append('Por favor Introduce la Contraseña')
        if (len(request.POST.get('password'))<5):
            errors.append('La Contraseña debe tener minimamente 5 caracteres.')
        if not request.POST.get('firstname', ''):
            errors.append('Por favor Introduce tu Nombre')
        if not request.POST.get('matricula',''):
            errors.append('Por favor Introduce tu Número de Matricula.')
        duplicadoMatricula = request.POST.get('matricula','')
        if duplicadoMatricula:
            if not duplicadoMatricula.isdigit():
                errors.append('Por favor llene Matricula solo con números.')
            else:
                duMA = User.objects.filter(matricula = duplicadoMatricula)
                if duMA:
                    errors.append('La Matricula ya existe')

        if not request.POST.get('ci',''):
            errors.append('Por favor Introduce tu Número de CI.')
        duplicadoCI =  request.POST.get('ci','')
        if duplicadoCI:
            if not duplicadoCI.isdigit():
                errors.append('Por favor Introduce CI solo con números')
            else:
                duCI = User.objects.filter(ci = duplicadoCI)
                if duCI:
                    errors.append('El CI ya existe.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Por favor Introduce una dirección de correo válida')
        if not errors:
            usuario = request.POST['username']
            contrasenia = request.POST['password']
            nombre = request.POST['firstname']
            apellido = request.POST['lastname']
            correo = request.POST['email']
            matricula = request.POST['matricula']
            ci = request.POST['ci']
            direccion = request.POST['direccion']
            # fecha = time.strftime("%y/%m/%d %H:%M:%S")
            account = User.objects.create_user(usuario, correo, contrasenia)
            account.first_name = nombre
            account.last_name = apellido
            account.matricula = matricula
            account.ci = ci
            account.direccion = direccion
            account.save()
            # return HttpResponse('<h1>usuario Creado Correctamente</h1>')
            ok = 'Cuenta creada Éxitosamente'
            return render(request, 'login.html', {'ok': ok})
        return render(request, 'register.html', {'errors': errors,
         'username': request.POST.get('username',''),
         'password':request.POST.get('password',''),
         'firstname':request.POST.get('firstname',''),
         'lastname':request.POST.get('lastname',''),
         'email': request.POST.get('email',''),
         'matricula': request.POST.get('matricula',''),
         'ci': request.POST.get('ci',''),
         'direccion': request.POST.get('direccion','')})

# def register_account(request):
#     user = User.objects.create_user('juan', 'juan@gmail.com', 'juan')
#     user.last_name = 'Perez'
#     user.first_name = 'Juanito'
#     user.telefono = 22211545
#     user.matricula = 8000961
#     user.ci = 7024740
#     user.save()
#     return HttpResponse('<h1>usuario Creado Correctamente</h1>')
