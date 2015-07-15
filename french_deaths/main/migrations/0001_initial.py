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
            ('cause', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.MorirCause'], null=True)),
        ))
        db.send_create_signal(u'main', ['Morir'])

        # Adding model 'MorirCause'
        db.create_table(u'main_morircause', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cause', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True)),
        ))
        db.send_create_signal(u'main', ['MorirCause'])


    def backwards(self, orm):
        # Deleting model 'Morir'
        db.delete_table(u'main_morir')

        # Deleting model 'MorirCause'
        db.delete_table(u'main_morircause')


    models = {
        u'main.morir': {
            'Meta': {'object_name': 'Morir'},
            'cause': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.MorirCause']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_deaths': ('django.db.models.fields.IntegerField', [], {'max_length': '15', 'null': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True'})
        },
        u'main.morircause': {
            'Meta': {'object_name': 'MorirCause'},
            'cause': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['main']