# Generated by Django 2.2 on 2019-06-05 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_products_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
    ]