# Generated by Django 3.2.9 on 2022-02-14 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0002_mainseo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainseo',
            options={'ordering': ('regular_url',), 'verbose_name': 'Seo', 'verbose_name_plural': 'Seo'},
        ),
    ]
