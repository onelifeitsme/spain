# Generated by Django 3.2.9 on 2022-02-14 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages_custom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatpageext',
            name='regular_url',
        ),
        migrations.RemoveField(
            model_name='flatpageext',
            name='seo_text',
        ),
    ]
