from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import FieldOption, FieldType, Risk, RiskType
from .utils import get_field_option, get_field_type


def create_or_update_field_options(filed_type, field_options, raise_exception=False):
    for field_option in field_options:
        field_option_instance = get_field_option(field_option.get("id", None), raise_exception)
        field_option["field_type"] = filed_type.id
        serializer = FieldOptionSerializer(instance=field_option_instance, data=field_option)
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationError(serializer.errors)


def create_or_update_field_types(field_types, risk_type_id=None, raise_exception=False):
    for field_type in field_types:
        field_options = field_type.pop("options")
        if risk_type_id:
            field_type["risk_type"] = risk_type_id
        field_type_instance = get_field_type(field_type.get("id", None), raise_exception=raise_exception)
        serializer = FieldTypeSerializer(field_type_instance, data=field_type)

        if serializer.is_valid():
            field_type_instance = serializer.save()
            create_or_update_field_options(field_type_instance, field_options, raise_exception=raise_exception)
        else:
            raise ValidationError(serializer.errors)


class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = ("id", "name", "data")


class FieldOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOption
        fields = ("id", "field_type", "choice", "label")


class FieldTypeSerializer(serializers.ModelSerializer):
    options = FieldOptionSerializer(many=True, read_only=True)

    class Meta:
        model = FieldType
        fields = ("id", "name", "risk_type", "label", "tooltip", "type", "visible", "hidden", "required", "options")


class RiskTypeSerializer(serializers.ModelSerializer):
    fields = FieldTypeSerializer(many=True, read_only=True)

    class Meta:
        model = RiskType
        fields = ("id", "name", "label", "description", "tooltip", "active", "created", "fields")

    def create_risk_type(self, owner, field_types):
        with transaction.atomic():
            risk_type_instance = self.save(owner=owner)
            create_or_update_field_types(field_types, risk_type_instance.id)

    def update_risk_type(self, field_types):
        with transaction.atomic():
            self.save()
            create_or_update_field_types(field_types, raise_exception=True)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    risk_types = RiskTypeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "risk_types")
