# Generated by Django 2.1.5 on 2019-01-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0008_auto_20190128_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_acct',
            name='baptised',
            field=models.CharField(default='Yes', max_length=20),
        ),
    ]