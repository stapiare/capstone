# Generated by Django 5.1 on 2024-08-30 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_usuario_cuestionario_cuestionario_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuestionario',
            name='usuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='cuestionario',
            field=models.ManyToManyField(blank=True, null=True, to='api.cuestionario'),
        ),
    ]
