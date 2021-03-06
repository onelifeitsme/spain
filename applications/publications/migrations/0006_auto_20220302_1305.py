# Generated by Django 3.2.9 on 2022-03-02 13:05

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_auto_20220301_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
        migrations.CreateModel(
            name='BlogTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='publications.blog')),
            ],
            options={
                'verbose_name': 'Blog Translation',
                'db_table': 'publications_blog_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
