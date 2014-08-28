# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VideoFragment'
        db.create_table(u'videoupload_videofragment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vidfile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('prev_video', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['videoupload.VideoFragment'])),
            ('next_video', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['videoupload.VideoFragment'])),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'videoupload', ['VideoFragment'])


    def backwards(self, orm):
        # Deleting model 'VideoFragment'
        db.delete_table(u'videoupload_videofragment')


    models = {
        u'videoupload.videofragment': {
            'Meta': {'object_name': 'VideoFragment'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'next_video': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['videoupload.VideoFragment']"}),
            'prev_video': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['videoupload.VideoFragment']"}),
            'vidfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['videoupload']