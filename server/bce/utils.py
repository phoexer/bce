import json
import os

from bce.models import FieldOption, FieldType, RiskType
from rest_framework.exceptions import ValidationError

dirname = os.path.dirname(__file__)


def load_file(file_name, subdirectory="tests/fixtures"):
    with open(os.path.join(dirname, subdirectory, file_name), encoding="utf-8") as data_file:
        return json.loads(data_file.read())


def get_field_option(pk, raise_exception=False):
    try:
        return FieldOption.objects.get(pk=pk)
    except FieldOption.DoesNotExist:
        if raise_exception:
            raise ValidationError("Field Option Does not exist.")
        return None


def get_field_type(pk, raise_exception=False):
    try:
        return FieldType.objects.get(pk=pk)
    except FieldType.DoesNotExist:
        if raise_exception:
            raise ValidationError("Field Type Does not exist.")
        return None


def get_risk_type(pk, raise_exception=False):
    try:
        return RiskType.objects.get(pk=pk)
    except RiskType.DoesNotExist:
        if raise_exception:
            raise ValidationError("Risk Type Does not exist.")
        return None
