# Generated by Django 3.2.9 on 2022-02-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_auto_20220215_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='text_0',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='text_5',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
