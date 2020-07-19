# Generated by Django 3.0.3 on 2020-03-09 12:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("bce", "0001_initial"),
        ("bce", "0002_auto_20181119_1632"),
        ("bce", "0003_auto_20181119_1700"),
        ("bce", "0004_auto_20181119_1702"),
        ("bce", "0005_auto_20181121_1622"),
        ("bce", "0006_auto_20200301_1937"),
    ]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RiskType",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("label", models.CharField(blank=True, default="", max_length=100)),
                ("description", models.TextField(blank=True)),
                ("tooltip", models.TextField(blank=True)),
                ("active", models.BooleanField(blank=True, default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="risk_types",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ("-created",),},
        ),
        migrations.CreateModel(
            name="FieldType",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("label", models.CharField(blank=True, default="", max_length=100)),
                ("tooltip", models.TextField(blank=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("TEXT", "Text Field"),
                            ("TEXTAREA", "Text Area"),
                            ("EMAIL", "Email Address"),
                            ("DATE", "Date"),
                            ("DATETIME", "Date and Time"),
                            ("NUMBER", "Numbers"),
                            ("CURRENCY", "Currency"),
                            ("RADIO", "Radio Buttons"),
                            ("DROPDOWN", "Dropdown Selection"),
                        ],
                        default="TEXT",
                        max_length=10,
                    ),
                ),
                ("visible", models.BooleanField(blank=True, default=True)),
                ("hidden", models.BooleanField(blank=True, default=False)),
                ("required", models.BooleanField(blank=True, default=False)),
                (
                    "risk_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="fields", to="bce.RiskType"
                    ),
                ),
            ],
            options={"ordering": ("id",),},
        ),
        migrations.CreateModel(
            name="Risk",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("data", models.CharField(max_length=102400)),
            ],
        ),
        migrations.CreateModel(
            name="FieldOption",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("choice", models.CharField(max_length=20)),
                ("label", models.CharField(max_length=100)),
                (
                    "field_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="options", to="bce.FieldType"
                    ),
                ),
            ],
            options={"ordering": ("choice",),},
        ),
    ]