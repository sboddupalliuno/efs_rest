# Generated by Django 3.0.7 on 2021-03-11 02:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio', '0002_mutualfund'),
    ]

    operations = [
        migrations.AddField(
            model_name='mutualfund',
            name='name',
            field=models.CharField(default='American', max_length=50),
            preserve_default=False,
        ),
    ]
