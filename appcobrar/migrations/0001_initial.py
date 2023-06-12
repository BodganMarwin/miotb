# Generated by Django 4.2.2 on 2023-06-11 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applectura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cobrar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de Cobro')),
                ('lectura', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='applectura.lectura', verbose_name='Lectura')),
            ],
            options={
                'db_table': 'cobrar',
                'managed': True,
            },
        ),
    ]
