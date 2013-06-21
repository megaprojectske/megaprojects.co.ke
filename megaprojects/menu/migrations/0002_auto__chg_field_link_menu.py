# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Link.menu'
        db.alter_column(u'menu_link', 'menu_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.Menu'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Link.menu'
        raise RuntimeError("Cannot reverse this migration. 'Link.menu' and its values cannot be restored.")

    models = {
        u'menu.link': {
            'Meta': {'ordering': "['menu', 'order', 'title']", 'object_name': 'Link'},
            'args': ('django.db.models.fields.CharField', [], {'default': "'[]'", 'max_length': '255', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kwargs': ('django.db.models.fields.CharField', [], {'default': "'{}'", 'max_length': '255', 'blank': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menu.Menu']", 'null': 'True', 'blank': 'True'}),
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