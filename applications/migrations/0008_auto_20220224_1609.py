# Generated by Django 3.2.9 on 2022-02-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0007_auto_20220216_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='reverse',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='icon_1',
            field=models.CharField(blank=True, default='flaticon-beach-house-2', max_length=200),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='icon_2',
            field=models.CharField(blank=True, default='flaticon-apartments', max_length=200),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='icon_3',
            field=models.CharField(blank=True, default='flaticon-student-housing', max_length=200),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='icon_4',
            field=models.CharField(blank=True, default='flaticon-modern-house-4', max_length=200),
        ),
    ]
