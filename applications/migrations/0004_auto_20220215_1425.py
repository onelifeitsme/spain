# Generated by Django 3.2.9 on 2022-02-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20220214_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='text_0',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_5',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_0',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_5',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
