from bce.models import FieldOption, FieldType, Risk, RiskType
from django.contrib.auth.models import User
from rest_framework import serializers


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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    risk_types = RiskTypeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "risk_types")
