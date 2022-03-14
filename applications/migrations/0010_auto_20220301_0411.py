# Generated by Django 3.2.9 on 2022-03-01 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0009_auto_20220301_0343'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsDetailInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('icon_1', models.CharField(blank=True, default='flaticon-beach-house-2', max_length=200)),
                ('title_1', models.CharField(blank=True, max_length=200)),
                ('title_1_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_1_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_1', models.CharField(blank=True, max_length=200)),
                ('subtitle_1_en', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_1_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('icon_2', models.CharField(blank=True, default='flaticon-apartments', max_length=200)),
                ('title_2', models.CharField(blank=True, max_length=200)),
                ('title_2_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_2_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_2', models.CharField(blank=True, max_length=200)),
                ('subtitle_2_en', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_2_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('icon_3', models.CharField(blank=True, default='flaticon-student-housing', max_length=200)),
                ('title_3', models.CharField(blank=True, max_length=200)),
                ('title_3_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_3_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_3', models.CharField(blank=True, max_length=200)),
                ('subtitle_3_en', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_3_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('icon_4', models.CharField(blank=True, default='flaticon-modern-house-4', max_length=200)),
                ('title_4', models.CharField(blank=True, max_length=200)),
                ('title_4_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_4_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_4', models.CharField(blank=True, max_length=200)),
                ('subtitle_4_en', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_4_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('reverse', models.BooleanField(default=False)),
                ('picture_2', models.ImageField(blank=True, upload_to='')),
                ('icon_6', models.CharField(blank=True, default='flaticon-beach-house-2', max_length=200)),
                ('title_6', models.CharField(blank=True, max_length=200)),
                ('title_6_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_6_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_6', models.CharField(blank=True, max_length=200)),
                ('subtitle_6_en', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_6_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('icon_7', models.CharField(blank=True, default='flaticon-apartments', max_length=200)),
                ('title_7', models.CharField(blank=True, max_length=200)),
                ('title_7_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_7_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_7', models.CharField(blank=True, max_length=200)),
                ('subtitle_7_en', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_7_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('icon_8', models.CharField(blank=True, default='flaticon-student-housing', max_length=200)),
                ('title_8', models.CharField(blank=True, max_length=200)),
                ('title_8_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_8_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_8', models.CharField(blank=True, max_length=200)),
                ('subtitle_8_en', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_8_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('icon_9', models.CharField(blank=True, default='flaticon-modern-house-4', max_length=200)),
                ('title_9', models.CharField(blank=True, max_length=200)),
                ('title_9_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_9_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_9', models.CharField(blank=True, max_length=200)),
                ('subtitle_9_en', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_9_ru', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='AboutUsText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_0', models.TextField(blank=True, max_length=10000)),
                ('text_0_en', models.TextField(blank=True, max_length=10000, null=True)),
                ('text_0_ru', models.TextField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.DeleteModel(
            name='AboutUs',
        ),
    ]
