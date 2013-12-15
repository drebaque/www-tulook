# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Marca.descripcion'
        db.add_column(u'principal_marca', 'descripcion',
                      self.gf('django.db.models.fields.CharField')(default=11111, max_length=120),
                      keep_default=False)

        # Adding field 'Marca.descripcionlarga'
        db.add_column(u'principal_marca', 'descripcionlarga',
                      self.gf('django.db.models.fields.TextField')(default=11111),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Marca.descripcion'
        db.delete_column(u'principal_marca', 'descripcion')

        # Deleting field 'Marca.descripcionlarga'
        db.delete_column(u'principal_marca', 'descripcionlarga')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'principal.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idcategoria': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'principal.datosempresa': {
            'Meta': {'object_name': 'DatosEmpresa'},
            'celular': ('django.db.models.fields.CharField', [], {'default': "'0261-xxxxxxxxx'", 'max_length': '15'}),
            'cuit': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'fotomapa': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'horarios': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkgooglemaps': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nfantasia': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'razonsocial': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "'0261-xxxxxxxxx'", 'max_length': '15'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'principal.marca': {
            'Meta': {'object_name': 'Marca'},
            'datos_contacto': ('django.db.models.fields.TextField', [], {}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'descripcionlarga': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idmarca': ('django.db.models.fields.IntegerField', [], {}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono_contacto': ('django.db.models.fields.CharField', [], {'default': "'0261-xxxxxxxxx'", 'max_length': '15'}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'principal.producto': {
            'Meta': {'object_name': 'Producto'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['principal.Categoria']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'destacado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idproducto': ('django.db.models.fields.IntegerField', [], {}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Marca']", 'null': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'precio': ('django.db.models.fields.CharField', [], {'default': "'Consultar'", 'max_length': '15'})
        },
        u'principal.promo': {
            'Meta': {'object_name': 'Promo'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fechafinalizacion': ('django.db.models.fields.DateField', [], {}),
            'fechainicio': ('django.db.models.fields.DateField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idpromo': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'precio': ('django.db.models.fields.CharField', [], {'default': "'Consultar'", 'max_length': '15'}),
            'prodpromo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['principal.Producto']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['principal']