# Generated by Django 2.1.5 on 2019-01-28 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0006_remove_t_acct_division'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_acct',
            name='spiritual_maturity',
        ),
        migrations.AddField(
            model_name='t_acct',
            name='member_status',
            field=models.CharField(default='Church Member', max_length=20),
        ),
    ]