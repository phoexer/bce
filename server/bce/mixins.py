from django.core.exceptions import ValidationError
from rest_framework import permissions

from .models import Risk
from .permissions import IsOwnerOrReadOnly
from .serializers import RiskSerializer, RiskTypeSerializer
from .utils import get_risk_type


class ValidateRiskTypeMixin:
    def validate_risk_type(self, request, risk_type_id=None, raise_exception=False):
        risk_type = get_risk_type(risk_type_id, raise_exception=raise_exception)
        try:
            field_types = request.data.pop("fields")
        except KeyError as error:
            raise ValidationError(error)
        serializer = RiskTypeSerializer(risk_type, data=request.data)
        serializer.is_valid(raise_exception=True)
        return field_types, serializer


class RiskListMixin:
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
