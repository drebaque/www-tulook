# -*- coding: utf-8 -*-
from principal.models import Categoria, Marca, Producto, Promo, DatosEmpresa
from django.contrib import admin

class PromoAdmin(admin.ModelAdmin):
	filter_horizontal = ('prodpromo',)
	list_display = ('nombre',)


admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Promo, PromoAdmin)
admin.site.register(DatosEmpresa)