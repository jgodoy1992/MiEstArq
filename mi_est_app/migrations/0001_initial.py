# Generated by Django 4.2 on 2023-11-15 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EnArriendo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128)),
                ('precio', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(max_length=128)),
                ('desc', models.TextField()),
                ('ancho', models.CharField(max_length=100)),
                ('largo', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
