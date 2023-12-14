# Generated by Django 5.0 on 2023-12-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0007_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaPaciente',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=70)),
                ('telefone', models.CharField(max_length=70)),
                ('cep', models.CharField(max_length=70)),
                ('logradouro', models.CharField(max_length=70)),
                ('bairro', models.CharField(max_length=70)),
                ('cidade', models.CharField(max_length=70)),
                ('estado', models.CharField(max_length=70)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=6)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tiposanguineo', models.CharField(max_length=3)),
            ],
        ),
    ]