# Generated by Django 4.2.4 on 2023-08-24 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_endereco_cliente_ativo_cliente_cpf_cliente_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='endereco',
        ),
    ]