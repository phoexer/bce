# Generated by Django 2.0.2 on 2018-11-19 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bce', '0002_auto_20181119_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='data',
            field=models.CharField(max_length=20480),
        ),
    ]
