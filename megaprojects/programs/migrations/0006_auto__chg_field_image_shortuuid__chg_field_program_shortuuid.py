# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Image.shortuuid'
        db.alter_column(u'programs_image', 'shortuuid', self.gf('core.fields.ShortUUIDField')(max_length=255, unique=True, null=True))

        # Changing field 'Program.shortuuid'
        db.alter_column(u'programs_program', 'shortuuid', self.gf('core.fields.ShortUUIDField')(max_length=255, unique=True, null=True))

    def backwards(self, orm):

        # Changing field 'Image.shortuuid'
        db.alter_column(u'programs_image', 'shortuuid', self.gf('core.fields.ShortUUIDField')(unique=True, max_length=22, null=True))

        # Changing field 'Program.shortuuid'
        db.alter_column(u'programs_program', 'shortuuid', self.gf('core.fields.ShortUUIDField')(unique=True, max_length=22, null=True))

    models = {
        u'programs.detail': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Detail'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Program']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'programs.image': {
            'Meta': {'ordering': "['program__title', '-created']", 'object_name': 'Image'},
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Program']"}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shortuuid': ('core.fields.ShortUUIDField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'thumbnail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'programs.program': {
            'Meta': {'ordering': "['title']", 'object_name': 'Program'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shortuuid': ('core.fields.ShortUUIDField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['programs']
