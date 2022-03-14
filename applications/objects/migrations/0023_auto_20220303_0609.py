# Generated by Django 3.2.9 on 2022-03-03 06:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('objects', '0022_auto_20220303_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentobject',
            name='amenities',
            field=models.ManyToManyField(blank=True, null=True, to='objects.Amenity'),
        ),
        migrations.AlterField(
            model_name='rentobject',
            name='favorites',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rentobject',
            name='type_of_deal',
            field=models.CharField(blank=True, choices=[('RENT', 'Rent'), ('SALE', 'Sale')], max_length=4, null=True, verbose_name='Type of deal'),
        ),
        migrations.AlterField(
            model_name='rentobject',
            name='type_rent_period',
            field=models.CharField(blank=True, choices=[('Per Night', 'Per Night'), ('Per Week', 'Per Week'), ('Per Month', 'Per Month')], default='Per Night', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='rentobjecttranslation',
            name='hidden_details',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Hidden details'),
        ),
        migrations.AlterField(
            model_name='rentobjecttranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='rentobjecttranslation',
            name='seo_description',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Meta description'),
        ),
        migrations.AlterField(
            model_name='rentobjecttranslation',
            name='seo_keywords',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Meta keywords'),
        ),
        migrations.AlterField(
            model_name='rentobjecttranslation',
            name='seo_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Meta title'),
        ),
        migrations.AlterField(
            model_name='rentobjecttranslation',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Text'),
        ),
    ]