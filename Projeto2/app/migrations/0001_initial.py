# Generated by Django 3.2.5 on 2021-07-19 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=5, verbose_name='Sigla')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('escudo', models.BinaryField()),
            ],
        ),
    ]
