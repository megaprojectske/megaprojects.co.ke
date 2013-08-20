# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Menu'
        db.create_table(u'menu_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'menu', ['Menu'])

        # Adding model 'Link'
        db.create_table(u'menu_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('view_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('args', self.gf('django.db.models.fields.CharField')(default='[]', max_length=255, blank=True)),
            ('kwargs', self.gf('django.db.models.fields.CharField')(default='{}', max_length=255, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.Link'], null=True, blank=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.Menu'])),
        ))
        db.send_create_signal(u'menu', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Menu'
        db.delete_table(u'menu_menu')

        # Deleting model 'Link'
        db.delete_table(u'menu_link')


    models = {
        u'menu.link': {
            'Meta': {'ordering': "['menu', 'order', 'title']", 'object_name': 'Link'},
            'args': ('django.db.models.fields.CharField', [], {'default': "'[]'", 'max_length': '255', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kwargs': ('django.db.models.fields.CharField', [], {'default': "'{}'", 'max_length': '255', 'blank': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menu.Menu']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menu.Link']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'view_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'menu.menu': {
            'Meta': {'ordering': "['title']", 'object_name': 'Menu'},
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['menu']
