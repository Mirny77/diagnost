# Generated by Django 2.1.5 on 2019-03-13 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='brand',
            field=models.CharField(max_length=10000, verbose_name='Марка автомобиля'),
        ),
        migrations.AlterField(
            model_name='recording',
            name='specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.Specialist', verbose_name='Специалист '),
        ),
    ]
