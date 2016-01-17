# -*- encoding:utf-8 -*-
from django.db import models

# Create your models here.
class Editor(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
		return '%d %s'%(self.id, self.nombre)

class TipoDocumento(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
		return '%d %s'%(self.id, self.descripcion)

class Area(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
		return '%d %s'%(self.id, self.descripcion)

class Estado(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
		return '%d %s'%(self.id, self.descripcion)

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
		return '%d %s %s'%(self.id, self.nombre, self.apellido)


class Libro(models.Model):
    codigo = models.CharField(max_length=10)
    titulo = models.CharField(max_length=50)
    autor = models.ManyToManyField(Autor)
    ejemplares = models.IntegerField()
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField()
    estado = models.ForeignKey(Estado)
    area = models.ForeignKey(Area)
    tipo_documento = models.ForeignKey(TipoDocumento)
    notas = models.TextField(blank=True)

    def __str__(self):
		return '%d %s %s %s %d %s %s %s %s %s'%(self.id, self.codigo, self.titulo, self.autor, self.ejemplares, self.editor, self.estado, self.area, self.tipo_documento, self.notas)


class Usuario(models.Model):
    usuario = models.CharField(max_length=30, unique = True)
    contrasenia = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    matricula = models.PositiveIntegerField(unique = True)
    telefono = models.IntegerField(null = True)
    ci = models.PositiveIntegerField(unique = True)
    email = models.EmailField(blank = True)
    tipo_usuario = models.BooleanField()

    def __str__(self):
        return '%d %s %s %s %s %d %d %d %s %d'%(self.id, self.usuario, self.contrasenia, self.nombre, self.apellidos, self.matricula, self.telefono, self.ci, self.email, self.tipo_usuario)

class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario)
    libro = models.ForeignKey(Libro)
    fecha_prestamo = models.DateField(auto_now_add = True)
    estado = models.CharField(max_length=20)
    fecha_maxDevolucion = models.DateTimeField()
    nota = models.TextField(blank = True)

    def __str__(self):
        return '%d %s %s %s %s'%(self.id, self.usuario, self.libro, self.estado, self.nota)

class Devolucion(models.Model):
    prestamo = models.ForeignKey(Prestamo)
    fecha_devolucion = models.DateField(auto_now_add = True)
    nota = models.TextField(blank = True)

    def __str__(self):
        return '%d %s %s'%(self.id, self.prestamo, self.nota)
