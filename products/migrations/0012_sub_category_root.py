# Generated by Django 2.2 on 2019-06-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_category',
            name='root',
            field=models.IntegerField(default=1),
        ),
    ]