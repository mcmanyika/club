# Generated by Django 2.1.5 on 2019-04-02 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0024_auto_20190228_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='how_you_know_us',
            field=models.CharField(blank=True, default='Not Applicable', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='part_you_enjoyed',
            field=models.CharField(blank=True, default='Not Applicable', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='recomendations',
            field=models.CharField(blank=True, default='Not Applicable', max_length=500, null=True),
        ),
    ]