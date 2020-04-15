from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .mixins import RiskListMixin, ValidateRiskTypeMixin
from .models import RiskType
from .serializers import RiskTypeSerializer


class ApiRoot(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response({"message": "you found the api, now what?"})


class RiskTypeList(ValidateRiskTypeMixin, APIView):
    def get(self, request):
        serializer = RiskTypeSerializer(RiskType.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            field_types, serializer = self.validate_risk_type(request)
            serializer.create_risk_type(owner=self.request.user, field_types=field_types)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


class RiskTypeDetail(ValidateRiskTypeMixin, APIView):
    def get(self, request, pk):
        risk_type = get_object_or_404(RiskType, pk=pk)
        serializer = RiskTypeSerializer(risk_type)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            field_types, serializer = self.validate_risk_type(request, risk_type_id=pk, raise_exception=True)
            serializer.update_risk_type(field_types)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        risk_type = get_object_or_404(RiskType, pk=pk)
        risk_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RiskList(RiskListMixin, generics.ListCreateAPIView):
    pass


class RiskDetail(RiskListMixin, generics.RetrieveUpdateDestroyAPIView):
    pass
