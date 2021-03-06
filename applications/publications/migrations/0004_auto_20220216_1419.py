# Generated by Django 3.2.9 on 2022-02-16 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publications', '0003_auto_20220216_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='seo_description_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta description'),
        ),
        migrations.AddField(
            model_name='blog',
            name='seo_description_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta description'),
        ),
        migrations.AddField(
            model_name='blog',
            name='seo_keywords_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Meta keywords'),
        ),
        migrations.AddField(
            model_name='blog',
            name='seo_keywords_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Meta keywords'),
        ),
        migrations.AddField(
            model_name='blog',
            name='seo_title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Meta title'),
        ),
        migrations.AddField(
            model_name='blog',
            name='seo_title_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Meta title'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='short_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='short_description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Short description'),
        ),
    ]
