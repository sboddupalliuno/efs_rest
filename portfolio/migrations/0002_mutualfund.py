# Generated by Django 3.0.7 on 2021-03-11 02:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutualFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=60)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('recent_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('recent_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mutualfunds',
                                               to='portfolio.Customer')),
            ],
        ),
    ]