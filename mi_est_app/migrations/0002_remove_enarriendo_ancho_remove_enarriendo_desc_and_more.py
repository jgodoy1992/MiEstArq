# Generated by Django 4.2 on 2023-11-13 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mi_est_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enarriendo',
            name='ancho',
        ),
        migrations.RemoveField(
            model_name='enarriendo',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='enarriendo',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='enarriendo',
            name='largo',
        ),
        migrations.RemoveField(
            model_name='enarriendo',
            name='tipo',
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(max_length=128)),
                ('desc', models.TextField()),
                ('ancho', models.CharField(max_length=100)),
                ('largo', models.CharField(max_length=100)),
                ('estacionamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_est_app.enarriendo')),
            ],
        ),
    ]
