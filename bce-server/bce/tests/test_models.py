import pytest
from bce.factories import FieldOptionFactory, FieldTypeFactory, RiskFactory, RiskTypeFactory


@pytest.mark.django_db
class TestRisk:
    def test_str(self):
        risk = RiskFactory()
        assert str(risk) == "vehicle"


@pytest.mark.django_db
class TestRiskType:
    def test_str(self):
        risk_type = RiskTypeFactory()
        assert str(risk_type) == "vehicle_risk_type"


@pytest.mark.django_db
class TestFieldType:
    def test_str(self):
        field_type = FieldTypeFactory()
        assert str(field_type) == "field_type"


@pytest.mark.django_db
class TestFieldOption:
    def test_str(self):
        field_option = FieldOptionFactory()
        assert str(field_option) == "label"
