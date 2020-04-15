import json
import os

from rest_framework.exceptions import ValidationError

from .models import FieldOption, FieldType, RiskType

dirname = os.path.dirname(__file__)


def load_file(file_name, subdirectory="tests/fixtures"):
    with open(os.path.join(dirname, subdirectory, file_name), encoding="utf-8") as data_file:
        return json.loads(data_file.read())


def get_object(cls, pk, raise_exception):
    try:
        return cls.objects.get(pk=pk)
    except cls.DoesNotExist:
        if raise_exception:
            raise ValidationError(f"{cls.__name__} Does not exist.")
        return None


def get_field_option(pk, raise_exception=False):
    return get_object(FieldOption, pk, raise_exception)


def get_field_type(pk, raise_exception=False):
    return get_object(FieldType, pk, raise_exception)


def get_risk_type(pk, raise_exception=False):
    return get_object(RiskType, pk, raise_exception)
