# Generated by Django 3.2.9 on 2022-03-03 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0024_alter_rentobjecttranslation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentobject',
            name='primary_image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='rentobject',
            name='type_of_deal',
            field=models.CharField(choices=[('RENT', 'Rent'), ('SALE', 'Sale')], max_length=4, null=True, verbose_name='Type of deal'),
        ),
        migrations.AlterField(
            model_name='rentobjecttranslation',
            name='name',
            field=models.CharField(default='New', max_length=255, null=True, verbose_name='Name'),
        ),
    ]
