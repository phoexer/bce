from django.contrib import admin

from .models import FieldOption, FieldType, Risk, RiskType

admin.site.register(Risk)
admin.site.register(RiskType)
admin.site.register(FieldType)
admin.site.register(FieldOption)
