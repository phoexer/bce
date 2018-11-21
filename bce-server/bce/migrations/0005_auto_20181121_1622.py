# Generated by Django 2.1.3 on 2018-11-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bce', '0004_auto_20181119_1702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fieldoption',
            options={'ordering': ('choice',)},
        ),
        migrations.AlterModelOptions(
            name='fieldtype',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='fieldtype',
            name='hidden',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='fieldtype',
            name='required',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='fieldtype',
            name='visible',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='risktype',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
