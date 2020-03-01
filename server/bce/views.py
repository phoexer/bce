from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Risk, RiskType
from .permissions import IsOwnerOrReadOnly
from .serializers import RiskSerializer, RiskTypeSerializer
from .utils import get_risk_type


class ApiRoot(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response({"message": "you found the api, now what?"})


class RiskTypeList(APIView):
    def get(self, request):
        serializer = RiskTypeSerializer(RiskType.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            field_types = request.data.pop("fields")
            serializer = RiskTypeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.create_risk_type(owner=self.request.user, field_types=field_types)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except KeyError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


class RiskTypeDetail(APIView):
    def get(self, request, pk):
        risk_type = get_object_or_404(RiskType, pk=pk)
        serializer = RiskTypeSerializer(risk_type)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            risk_type = get_risk_type(pk, raise_exception=True)
            field_types = request.data.pop("fields")
            serializer = RiskTypeSerializer(risk_type, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.update_risk_type(field_types)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        risk_type = get_object_or_404(RiskType, pk=pk)
        risk_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RiskList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer


class RiskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
