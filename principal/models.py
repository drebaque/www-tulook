# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
# from imagekit.models import ImageSpecField
# from imagekit.processors import ResizeToFill, Adjust

class Categoria(models.Model):
	idcategoria = models.IntegerField()
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.nombre

class Marca(models.Model):
	idmarca = models.IntegerField()
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()
	web = models.CharField(max_length=150)
	# logo = models.ImageField(upload_to='logo')
	datos_contacto = models.TextField()
	telefono_contacto = models.CharField(max_length=15, default="0261-xxxxxxxxx")

	def __unicode__(self):
		return self.nombre


class Producto(models.Model):
	idproducto = models.IntegerField()
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()
	# foto = models.ImageField(upload_to='producto')
	destacado = models.BooleanField()
	precio = models.CharField(max_length=15, default="Consultar") #se puede poner por default: Consultar - y en alguna promo el valor que se desee
	categoria = models.ForeignKey(Categoria, default=1)
	marca = models.ForeignKey(Marca, null=True)

	def __unicode__(self):
		return self.nombre

class Promo(models.Model):
	idpromo = models.IntegerField()
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()
	# foto = models.ImageField(upload_to='producto') foto de los productos de la promo
	precio = models.CharField(max_length=15, default="Consultar") #se puede poner por default: Consultar - y en alguna promo el valor que se desee
	fechainicio = models.DateField()
	fechafinalizacion = models.DateField()
	prodpromo = models.ManyToManyField(Producto, blank=True, null=True)

	def __unicode__(self):
		return self.nombre


class DatosEmpresa(models.Model):
	razonsocial = models.CharField(max_length=30)
	nfantasia = models.CharField(max_length=30)
	cuit = models.CharField(max_length=11)
	direccion = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	telefono = models.CharField(max_length=15, default="0261-xxxxxxxxx")
	celular = models.CharField(max_length=15, default="0261-xxxxxxxxx")
	horarios = models.CharField(max_length=30)
	linkgooglemaps = models.CharField(max_length=100)
	# fotomapa = models.ImageField(upload_to='empresa', verbose_name='mapa')
	usuario = models.ForeignKey(User)

	def __unicode__(self):
	  	return self.razonsocial

