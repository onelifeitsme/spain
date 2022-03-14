# Generated by Django 3.2.9 on 2022-03-02 10:44

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0015_auto_20220301_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutusdetailinformation',
            name='icon_2',
        ),
        migrations.RemoveField(
            model_name='aboutusdetailinformation',
            name='icon_3',
        ),
        migrations.RemoveField(
            model_name='aboutusdetailinformation',
            name='icon_4',
        ),
        migrations.RemoveField(
            model_name='aboutusdetailinformation',
            name='subtitle_1',
        ),
        migrations.RemoveField(
            model_name='aboutusdetailinformation',
            name='subtitle_2',
        ),
        migrations.RemoveField(
            model_name='aboutusdetailinformation',
            name='subtitle_3',
        ),
        migrations.RemoveField(
            model_name='aboutusdetailinformation',
            name='subtitle_4',
        ),
        migrations.RemoveField(
            model_name='aboutusdetailinformation',
            name='title_1',
        ),
        migrations.RemoveField(
            model_name='aboutusdetailinformation',
            name='title_2',
        ),
        migrations.RemoveField(
            model_name='aboutusdetailinformation',
            name='title_3',
        ),
        migrations.RemoveField(
            model_name='aboutusdetailinformation',
            name='title_4',
        ),
        migrations.CreateModel(
            name='AboutUsDetailInformationTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title_1', models.CharField(blank=True, max_length=200)),
                ('subtitle_1', models.CharField(blank=True, max_length=200)),
                ('title_2', models.CharField(blank=True, max_length=200)),
                ('subtitle_2', models.CharField(blank=True, max_length=200)),
                ('title_3', models.CharField(blank=True, max_length=200)),
                ('subtitle_3', models.CharField(blank=True, max_length=200)),
                ('title_4', models.CharField(blank=True, max_length=200)),
                ('subtitle_4', models.CharField(blank=True, max_length=200)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='applications.aboutusdetailinformation')),
            ],
            options={
                'verbose_name': 'About Us Detail Information Translation',
                'db_table': 'applications_aboutusdetailinformation_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
