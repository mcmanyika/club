# Generated by Django 2.2 on 2019-04-26 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='rootid',
        ),
    ]