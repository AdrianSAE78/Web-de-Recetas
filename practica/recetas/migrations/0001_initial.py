# Generated by Django 4.2 on 2024-07-13 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('P', 'Postre'), ('F', 'Plato Fuerte'), ('B', 'Bebida'), ('E', 'Entrada')], max_length=30)),
                ('ingredients', models.CharField(max_length=500)),
            ],
        ),
    ]
