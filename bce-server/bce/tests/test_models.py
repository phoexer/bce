import pytest
from bce.models import Risk


@pytest.mark.django_db
class TestRisk:
    def test_str(self):
        risk = Risk(name="test")
        assert str(risk) == "test"
