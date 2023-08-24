# Generated by Django 4.2.4 on 2023-08-24 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cliente_delete_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9, null=True)),
                ('estado', models.CharField(max_length=100, null=True)),
                ('cidade', models.CharField(max_length=100, null=True)),
                ('bairro', models.CharField(max_length=100, null=True)),
                ('logradouro', models.CharField(max_length=100, null=True)),
                ('numero', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='ativo',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='sexo',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ManyToManyField(to='core.endereco'),
        ),
    ]