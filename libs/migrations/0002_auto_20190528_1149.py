# Generated by Django 2.2 on 2019-05-28 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_discussion',
            name='header',
            field=models.CharField(max_length=50),
        ),
    ]