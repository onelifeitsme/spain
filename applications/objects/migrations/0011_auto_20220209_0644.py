# Generated by Django 3.2.9 on 2022-02-09 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0010_merge_20220204_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='seo_text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='rentobject',
            name='seo_text',
            field=models.TextField(null=True),
        ),
    ]