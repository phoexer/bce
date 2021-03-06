from django.db import models

from .constants import DEFAULT_FIELD_TYPES, FIELD_TYPE_TEXT


class Risk(models.Model):
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=102400)

    def __str__(self):
        return self.name


class RiskType(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100, blank=True, default="")
    description = models.TextField(blank=True)
    tooltip = models.TextField(blank=True)
    active = models.BooleanField(default=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("auth.User", related_name="risk_types", on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name


class FieldType(models.Model):
    name = models.CharField(max_length=100)
    risk_type = models.ForeignKey("RiskType", related_name="fields", on_delete=models.CASCADE)
    label = models.CharField(max_length=100, blank=True, default="")
    tooltip = models.TextField(blank=True)
    type = models.CharField(max_length=10, choices=DEFAULT_FIELD_TYPES, default=FIELD_TYPE_TEXT)
    visible = models.BooleanField(default=True, blank=True)
    hidden = models.BooleanField(default=False, blank=True)
    required = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.name


class FieldOption(models.Model):
    choice = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    field_type = models.ForeignKey("FieldType", related_name="options", on_delete=models.CASCADE)

    class Meta:
        ordering = ("choice",)

    def __str__(self):
        return self.label
