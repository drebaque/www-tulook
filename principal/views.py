# -*- coding: utf-8 -*-
# Create your views here.
from principal.models import Categoria, Marca, Producto, Promo, DatosEmpresa
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
	marca = Marca.objects.all()
	promociones = Promo.objects.all()
	return render_to_response('index.html',{'marca':marca, 'promociones':promociones})

def productos(request):
	productos = Producto.objects.exclude(categoria__nombre__in=['TRATAMIENTOS','TERAPIAS','SERVICIOS'])
	return render_to_response('productos.html',{'productos':productos})

def lista_productos(request):
	productos = Producto.objects.all()
	return render_to_response('lista_productos.html',{'lista':productos})

def lista_datosempresa(request):
	datos = DatosEmpresa.objects.all()
	return render_to_response('lista_datosempresa.html',{'lista':datos})

def categorias(request):
	categorias = Categoria.objects.all()
	return render_to_response('categorias.html',{'categorias':categorias}, context_instance=RequestContext(request))

def lista_categorias(request):
	categoria = Categoria.objects.all()
	return render_to_response('lista_categorias.html',{'categoria':categoria}, context_instance=RequestContext(request))

def detalle_categorias_productos(request, id_categoria):
	dato = get_object_or_404(Categoria, pk=id_categoria)
	productos = Producto.objects.filter(categoria=dato)
	return render_to_response('categorias_productos.html',{'categoria':dato, 'productos':productos}, context_instance=RequestContext(request))

def detalle_producto(request, id_producto):
	dato = get_object_or_404(Producto, pk=id_producto)
	return render_to_response('producto.html',{'producto':dato}, context_instance=RequestContext(request))

def lista_marcas(request):
	marca = Marca.objects.all()
	return render_to_response('lista_marcas.html',{'marca':marca})

def tratamientos(request):
	productos = Producto.objects.filter(categoria__nombre='TRATAMIENTOS')
	return render_to_response('tratamientos.html',{'productos':productos})

def terapias(request):
	productos = Producto.objects.filter(categoria__nombre='TERAPIAS')
	return render_to_response('terapias.html',{'productos':productos})

def servicios(request):
	productos = Producto.objects.filter(categoria__nombre='SERVICIOS')
	return render_to_response('servicios.html',{'productos':productos})

def promociones(request):
	promociones = Promo.objects.all()
	return render_to_response('promociones.html',{'promociones':promociones})
