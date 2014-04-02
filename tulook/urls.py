# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'principal.views.index'),
	url(r'^inicio/$', 'principal.views.index'),
	#url(r'^$', 'principal.views.lista_productos'),
	#url(r'^$', 'principal.views.lista_marcas'),
	#url(r'^$', 'principal.views.lista_datosempresa'),
	url(r'^productos/$', 'principal.views.productos'),
	url(r'^categorias/$', 'principal.views.categorias'),
	url(r'^marcas/$', 'principal.views.lista_marcas'),
	url(r'^tratamientos/$', 'principal.views.tratamientos'),
	url(r'^terapias/$', 'principal.views.terapias'),
	url(r'^servicios/$', 'principal.views.servicios'),
	#url(r'^promociones/$', 'principal.views.promociones'),
	# url(r'^categorias/$', 'principal.views.lista_categorias'),
	url(r'^categorias_productos/(?P<id_categoria>\d+)$','principal.views.detalle_categorias_productos'),
	url(r'^productos/(?P<id_producto>\d+)$','principal.views.detalle_producto'),
	url(r'^promociones/(?P<id_promo>\d+)$','principal.views.promociones'),
	url(r'^contacto/', include('contact_form.urls')),
	# url(r'^tulook/', include('tulook.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),	
	)
