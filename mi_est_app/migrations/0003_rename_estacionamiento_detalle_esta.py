# Generated by Django 4.2 on 2023-11-13 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_est_app', '0002_remove_enarriendo_ancho_remove_enarriendo_desc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalle',
            old_name='estacionamiento',
            new_name='esta',
        ),
    ]
