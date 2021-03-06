# Generated by Django 3.2.9 on 2022-03-01 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0008_auto_20220224_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='icon_6',
            field=models.CharField(blank=True, default='flaticon-beach-house-2', max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='icon_7',
            field=models.CharField(blank=True, default='flaticon-apartments', max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='icon_8',
            field=models.CharField(blank=True, default='flaticon-student-housing', max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='icon_9',
            field=models.CharField(blank=True, default='flaticon-modern-house-4', max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='picture_2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_6',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_7',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_8',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_9',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_6',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_7',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_8',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_9',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
