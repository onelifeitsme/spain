# Generated by Django 3.2.9 on 2021-12-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0003_rentobject_type_rent_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentobject',
            name='type_rent_period',
            field=models.CharField(choices=[('Per Night', 'Per Night'), ('Per Week', 'Per Week'), ('Per Month', 'Per Month')], max_length=10, null=True),
        ),
    ]
