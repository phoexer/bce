import factory
from bce.models import FieldOption, FieldType, Risk, RiskType
from django.contrib.auth.models import User


class RiskFactory(factory.DjangoModelFactory):
    class Meta:
        model = Risk

    name = "vehicle"


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = "admin"


class RiskTypeFactory(factory.DjangoModelFactory):
    class Meta:
        model = RiskType
        django_get_or_create = ("name",)

    name = "vehicle_risk_type"
    owner = factory.SubFactory(UserFactory)


class FieldTypeFactory(factory.DjangoModelFactory):
    class Meta:
        model = FieldType

    name = "field_type"
    risk_type = factory.SubFactory(RiskTypeFactory)


class FieldOptionFactory(factory.DjangoModelFactory):
    class Meta:
        model = FieldOption

    label = "label"
    field_type = factory.SubFactory(FieldTypeFactory)
    choice = ""
