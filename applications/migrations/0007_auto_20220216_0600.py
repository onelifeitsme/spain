# Generated by Django 3.2.9 on 2022-02-16 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0006_auto_20220216_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_1_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_1_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_2_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_2_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_3_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_3_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_4_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_4_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_little_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_little_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_0_en',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_0_ru',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_5_en',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_5_ru',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_1_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_1_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_2_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_2_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_3_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_3_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_4_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_4_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_5_en',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_5_ru',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_little_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_little_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
