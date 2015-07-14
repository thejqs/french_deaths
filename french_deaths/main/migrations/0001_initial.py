# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Morir'
        db.create_table(u'main_morir', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number_of_deaths', self.gf('django.db.models.fields.IntegerField')(max_length=15, null=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=8, null=True)),
            ('cause_of_death', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'main', ['Morir'])


    def backwards(self, orm):
        # Deleting model 'Morir'
        db.delete_table(u'main_morir')


    models = {
        u'main.morir': {
            'Meta': {'object_name': 'Morir'},
            'cause_of_death': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_deaths': ('django.db.models.fields.IntegerField', [], {'max_length': '15', 'null': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True'})
        }
    }

    complete_apps = ['main']