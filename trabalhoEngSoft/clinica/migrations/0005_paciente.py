# Generated by Django 5.0 on 2023-12-13 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0004_agenda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('peso', models.DecimalField(decimal_places=2, max_digits=6)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tiposanguineo', models.CharField(max_length=3)),
                ('codigo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='clinica.pessoa')),
            ],
        ),
    ]