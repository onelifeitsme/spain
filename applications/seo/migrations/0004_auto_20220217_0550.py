# Generated by Django 3.2.9 on 2022-02-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0003_alter_mainseo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainseo',
            options={'ordering': ('url',), 'verbose_name': 'Seo', 'verbose_name_plural': 'Seo'},
        ),
        migrations.RemoveField(
            model_name='mainseo',
            name='regular_url',
        ),
        migrations.AddField(
            model_name='mainseo',
            name='seo_description_en',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Meta description'),
        ),
        migrations.AddField(
            model_name='mainseo',
            name='seo_description_ru',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Meta description'),
        ),
        migrations.AddField(
            model_name='mainseo',
            name='seo_keywords_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Meta keywords'),
        ),
        migrations.AddField(
            model_name='mainseo',
            name='seo_keywords_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Meta keywords'),
        ),
        migrations.AddField(
            model_name='mainseo',
            name='seo_text_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mainseo',
            name='seo_text_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mainseo',
            name='seo_title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Meta title'),
        ),
        migrations.AddField(
            model_name='mainseo',
            name='seo_title_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Meta title'),
        ),
        migrations.AddField(
            model_name='mainseo',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
