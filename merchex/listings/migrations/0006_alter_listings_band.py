# Generated by Django 4.0.1 on 2022-04-05 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_listings_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='band',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]
