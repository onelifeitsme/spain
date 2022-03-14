# Generated by Django 3.2.9 on 2022-03-03 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0019_auto_20220303_0348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentobject',
            name='seo_description',
        ),
        migrations.RemoveField(
            model_name='rentobject',
            name='seo_keywords',
        ),
        migrations.RemoveField(
            model_name='rentobject',
            name='seo_title',
        ),
        migrations.AddField(
            model_name='rentobjecttranslation',
            name='seo_description',
            field=models.TextField(blank=True, max_length=255, verbose_name='Meta description'),
        ),
        migrations.AddField(
            model_name='rentobjecttranslation',
            name='seo_keywords',
            field=models.CharField(blank=True, max_length=100, verbose_name='Meta keywords'),
        ),
        migrations.AddField(
            model_name='rentobjecttranslation',
            name='seo_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Meta title'),
        ),
    ]
