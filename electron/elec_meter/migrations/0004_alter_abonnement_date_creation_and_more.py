# Generated by Django 4.0.5 on 2022-08-15 12:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('elec_meter', '0003_alter_abonnement_date_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonnement',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2022, 8, 15, 12, 12, 24, 152879, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 12, 12, 24, 143497, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='infosignal',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 12, 12, 24, 147596, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='retrait',
            name='heure_retrait',
            field=models.TimeField(default='14:12:24'),
        ),
        migrations.AlterField(
            model_name='retrait',
            name='jour_retrait',
            field=models.DateField(default=datetime.datetime(2022, 8, 15, 14, 12, 24, 157842)),
        ),
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.FloatField(default=0.0)),
                ('date_achat', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='acheteur', to='elec_meter.machine')),
                ('trader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='vendeur', to='elec_meter.machine')),
            ],
            options={
                'db_table': 'ACHAT',
            },
        ),
    ]
