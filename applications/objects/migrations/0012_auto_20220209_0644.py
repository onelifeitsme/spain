# Generated by Django 3.2.9 on 2022-02-09 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0011_auto_20220209_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='seo_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rentobject',
            name='seo_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]