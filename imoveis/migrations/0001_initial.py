# Generated by Django 4.0 on 2021-12-12 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=255)),
                ('areaconstruida', models.CharField(max_length=100)),
                ('situacao', models.CharField(max_length=100)),
                ('observacao', models.TextField(blank=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='imoveis.tipo')),
            ],
        ),
    ]
