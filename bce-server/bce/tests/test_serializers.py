import pytest
from bce.factories import FieldOptionFactory, FieldTypeFactory, RiskFactory, RiskTypeFactory, UserFactory
from bce.serializers import (
    FieldOptionSerializer,
    FieldTypeSerializer,
    RiskSerializer,
    RiskTypeSerializer,
    UserSerializer,
)


@pytest.mark.django_db
class TestRiskSerializer:
    def test_serialization(self):
        risk = RiskFactory()
        serializer = RiskSerializer(instance=risk)
        data = serializer.data
        assert set(data.keys()) == {
            "id",
            "name",
            "data",
        }


@pytest.mark.django_db
class TestFieldOptionSerializer:
    def test_serialization(self):
        field_option = FieldOptionFactory()
        serializer = FieldOptionSerializer(instance=field_option)
        data = serializer.data
        assert set(data.keys()) == {"id", "field_type", "choice", "label"}


@pytest.mark.django_db
class TestFieldTypeSerializer:
    def test_serialization(self):
        field_type = FieldTypeFactory()
        serializer = FieldTypeSerializer(instance=field_type)
        data = serializer.data
        assert set(data.keys()) == {
            "id",
            "name",
            "risk_type",
            "label",
            "tooltip",
            "type",
            "visible",
            "hidden",
            "required",
            "options",
        }


@pytest.mark.django_db
class TestRiskTypeSerializer:
    def test_serialization(self):
        risk_type = RiskTypeFactory()
        serializer = RiskTypeSerializer(instance=risk_type)
        data = serializer.data
        assert set(data.keys()) == {"id", "name", "label", "description", "tooltip", "active", "created", "fields"}


@pytest.mark.django_db
class TestUserSerializer:
    def test_serialization(self):
        user = UserFactory()
        serializer = UserSerializer(instance=user)
        data = serializer.data
        assert set(data.keys()) == {"id", "username", "risk_types"}
