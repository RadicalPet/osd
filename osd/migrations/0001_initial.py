# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 01:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('company', models.TextField(blank=True, max_length=200)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('abstract', models.TextField(blank=True, max_length=1000)),
                ('accepted', models.BooleanField(default=False)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('length', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osd.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('company', models.TextField(blank=True, max_length=200)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('abstract', models.TextField(blank=True, max_length=1000)),
                ('confirmed', models.BooleanField(default=False)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osd.Session')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=360)),
                ('logo', models.CharField(blank=True, max_length=60)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('contact_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='sponsor',
            name='sponsor_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osd.SponsorType'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osd.Session'),
        ),
    ]
