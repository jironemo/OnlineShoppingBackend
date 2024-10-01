# Generated by Django 5.0.7 on 2024-08-12 11:51

import pictures.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=pictures.models.PictureField(aspect_ratios=[None], blank=True, breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, file_types=['WEBP'], grid_columns=12, height_field=1000, pixel_densities=[1, 2], upload_to='previews', width_field=1000),
        ),
    ]