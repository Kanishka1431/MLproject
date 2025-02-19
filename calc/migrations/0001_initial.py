# Generated by Django 5.0.7 on 2024-11-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HousePriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.FloatField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('garage', models.IntegerField()),
                ('predicted_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
