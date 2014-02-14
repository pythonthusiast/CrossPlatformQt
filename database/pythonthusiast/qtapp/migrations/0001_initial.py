# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Users'
        db.create_table('qtapp_users', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('qtapp', ['Users'])


    def backwards(self, orm):
        # Deleting model 'Users'
        db.delete_table('qtapp_users')


    models = {
        'qtapp.users': {
            'Meta': {'object_name': 'Users'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['qtapp']