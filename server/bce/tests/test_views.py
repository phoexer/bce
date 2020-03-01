import pytest
from bce import views
from bce.factories import RiskTypeFactory
from bce.models import RiskType
from bce.utils import load_file
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate


@pytest.mark.django_db
class TestRiskTypeListAPIView:
    @pytest.fixture(autouse=True)
    def setup_tests(self):
        self.api_request_factory = APIRequestFactory()
        self.user = User.objects.create_user("testuser", "password")
        self.create_endpoint = reverse("risk-type-list")

    def _get_payload(self):
        return load_file("risktype_l3.json")

    def _send_list_request(self, authenticate=True):
        list_url = reverse("risk-type-list")
        request = self.api_request_factory.get(list_url)
        if authenticate:
            force_authenticate(request, user=self.user)
        return views.RiskTypeList.as_view()(request)

    def _send_create_request(self, payload=None, authenticate=True):
        payload = payload if payload is not None else self._get_payload()
        request = self.api_request_factory.post(self.create_endpoint, payload, format="json")
        if authenticate:
            force_authenticate(request, user=self.user)
        return views.RiskTypeList.as_view()(request)

    def test_list_risk_types(self):
        RiskTypeFactory(name="vehicle_risk_type1", owner=self.user)
        RiskTypeFactory(name="vehicle_risk_type2", owner=self.user)
        RiskTypeFactory(name="vehicle_risk_type3", owner=self.user)
        response = self._send_list_request()
        new_risk_types = response.data
        assert response.status_code == status.HTTP_200_OK
        assert len(new_risk_types) == 3
        assert new_risk_types[0]["name"] == "vehicle_risk_type1"
        assert new_risk_types[1]["name"] == "vehicle_risk_type2"
        assert new_risk_types[2]["name"] == "vehicle_risk_type3"

    def test_list_risk_types_without_authentication(self):
        RiskTypeFactory(name="vehicle_risk_type1", owner=self.user)
        response = self._send_list_request(authenticate=False)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_risk_type(self):
        response = self._send_create_request()
        assert response.status_code == status.HTTP_201_CREATED
        print(response.data)
        new_risk_type = response.data
        assert new_risk_type.get("id") is not None
        assert new_risk_type["name"] == "Auto-Insurance"
        assert new_risk_type["label"] == "Sample Label"
        assert len(new_risk_type["fields"]) == 7

    def test_create_risk_type_without_authentication(self):
        response = self._send_create_request(authenticate=False)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_risk_type_with_empty_payload(self):
        response = self._send_create_request(payload={})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_with_bad_json(self):
        risk_type_count = RiskType.objects.count()

        data1 = load_file("risktype_l3_err1.json")
        data2 = load_file("risktype_l3_err2.json")

        response = self._send_create_request(payload=data1)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert RiskType.objects.count() == risk_type_count

        response = self._send_create_request(payload=data2)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert RiskType.objects.count() == risk_type_count


@pytest.mark.django_db
class TestRiskTypeDetailAPIView:
    @pytest.fixture(autouse=True)
    def setup_tests(self):
        self.api_request_factory = APIRequestFactory()
        self.user = User.objects.create_user("testuser", "password")
        risk_type = self._send_create_request().data
        self.risk_type = RiskType.objects.get(id=risk_type["id"])

    def _get_payload(self):
        return load_file("risktype_l2.json")

    def _send_create_request(self, payload=None, authenticate=True):
        payload = payload if payload is not None else self._get_payload()
        create_endpoint = reverse("risk-type-list")
        request = self.api_request_factory.post(create_endpoint, payload, format="json")
        if authenticate:
            force_authenticate(request, user=self.user)
        return views.RiskTypeList.as_view()(request)

    def _get_risk_type(self, risk_type_id=None, authenticate=True):
        risk_type_id = risk_type_id if risk_type_id is not None else self.risk_type.id
        get_url = reverse("risk-type-detail", kwargs={"pk": self.risk_type.id})
        request = self.api_request_factory.get(get_url, format="json")
        if authenticate:
            force_authenticate(request, user=self.user)
        return views.RiskTypeDetail.as_view()(request, pk=self.risk_type.id)

    def _send_edit_request(self, payload=None, authenticate=True):
        payload = payload if payload is not None else self._get_payload()
        url = reverse("risk-type-detail", kwargs={"pk": self.risk_type.id})
        request = self.api_request_factory.put(url, payload, format="json")
        if authenticate:
            force_authenticate(request, user=self.user)
        return views.RiskTypeDetail.as_view()(request, pk=self.risk_type.id)

    def _send_delete_request(self, authenticate=True):
        url = reverse("risk-type-detail", kwargs={"pk": self.risk_type.id})
        request = self.api_request_factory.delete(url, format="json")
        if authenticate:
            force_authenticate(request, user=self.user)
        return views.RiskTypeDetail.as_view()(request, pk=self.risk_type.id)

    def test_edit_risk_type(self):
        payload = self._get_risk_type().data
        payload["label"] = "new label"
        payload["fields"][0]["tooltip"] = "New Tool tip"
        response = self._send_edit_request(payload)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["label"] == "new label"
        assert response.data["fields"][0]["tooltip"] == "New Tool tip"

    def test_delete_risk_type(self):
        risk_type = self._get_risk_type().data

        response = self._send_delete_request()
        assert response.status_code == status.HTTP_204_NO_CONTENT

        response = self._get_risk_type(risk_type["id"])
        assert response.status_code == status.HTTP_404_NOT_FOUND
