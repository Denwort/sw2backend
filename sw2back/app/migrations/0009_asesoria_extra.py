# Generated by Django 5.0.4 on 2024-07-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_estudiante_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='asesoria',
            name='extra',
            field=models.BooleanField(default=False),
        ),
    ]
