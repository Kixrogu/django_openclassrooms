# Generated by Django 4.0.1 on 2022-04-05 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_alter_listings_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.artist'),
        ),
    ]
