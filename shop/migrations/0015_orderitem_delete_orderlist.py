# Generated by Django 5.1 on 2024-09-30 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_cartproducts_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.TextField(default='pending')),
                ('order', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='OrderList',
        ),
    ]
