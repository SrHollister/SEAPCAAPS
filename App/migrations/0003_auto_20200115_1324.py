# Generated by Django 2.2.7 on 2020-01-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_pacientes_id_edocivil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='Telefono',
            field=models.CharField(max_length=10),
        ),
    ]