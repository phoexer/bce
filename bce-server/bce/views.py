from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from bce.models import RiskType, FieldType, FieldOption, Risk
from rest_framework.parsers import JSONParser
from rest_framework import generics
from bce.serializers import RiskTypeSerializer, FieldTypeSerializer, FieldOptionSerializer, RiskSerializer
from rest_framework import permissions
from bce.permissions import IsOwnerOrReadOnly
from django.db import transaction
from django.template import loader
from django.http import HttpResponse


# class ApiRoot(APIView):
#     def get(self, request, format=None):
#         return Response({
#             'message': 'you found the api, now what?'
#         })

def index(request):
    # template = loader.get_template('home.html')
    # context = {}
    # return HttpResponse(template.render(context, request))
    return render(request, 'home.html')


class RiskTypeList(APIView):
    def get(self, request, formart=None):
        # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
        serializer = RiskTypeSerializer(RiskType.objects.all(), many=True)
        return Response(serializer.data)

    @transaction.atomic
    def post(self, request, format=None):
        field_types = request.data.pop('fields')

        serializer = RiskTypeSerializer(data=request.data)

        sp1 = transaction.savepoint()
        if serializer.is_valid():
            risk_type_inst = serializer.save(owner=self.request.user)
#            print(risk_type_inst)

            for field_type in field_types:
                field_options = field_type.pop('options')

                field_type['risk_type'] = risk_type_inst.id
                ft_serializer = FieldTypeSerializer(data=field_type)

                if ft_serializer.is_valid():
                    filed_type_inst = ft_serializer.save()

                    for field_option in field_options:
                        field_option['field_type'] = filed_type_inst.id
                        fo_serializer = FieldOptionSerializer(data=field_option)
                        if fo_serializer.is_valid():
                            fo_serializer.save()
                        else:
                            transaction.savepoint_rollback(sp1)
                            return Response(fo_serializer.data, status=status.HTTP_400_BAD_REQUEST)
                else:
                    transaction.savepoint_rollback(sp1)
                    return Response(ft_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            transaction.savepoint_commit(sp1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            transaction.savepoint_rollback(sp1)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiskTypeDetail(APIView):
    def get_risk_type(self, pk):
        try:
            return RiskType.objects.get(pk=pk)
        except RiskType.DoesNotExist:
            raise Http404

    def get_field_type(self, pk):
        try:
            return FieldType.objects.get(pk=pk)
        except RiskType.DoesNotExist:
            raise Http404

    def get_field_option(self, pk):
        try:
            return FieldOption.objects.get(pk=pk)
        except RiskType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        risk_type = self.get_risk_type(pk)
        serializer = RiskTypeSerializer(risk_type)
        return Response(serializer.data)

    @transaction.atomic
    def put(self, request, pk, format=None):
        risk_type = self.get_risk_type(pk)
        data = JSONParser().parse(request)

        field_types = data.pop('fields')

        sp1 = transaction.savepoint()

        serializer = RiskTypeSerializer(risk_type, data=data)
        if serializer.is_valid():
            serializer.save()

            for field_type in field_types:
                field_options = field_type.pop('options')

                field_type_inst = self.get_field_type(field_type["id"])
                ft_serializer = FieldTypeSerializer(field_type_inst, data=field_type)

                if ft_serializer.is_valid():
                    ft_serializer.save()

                    for field_option in field_options:
                        field_option_inst = self.get_field_option(field_option["id"])
                        fo_serializer = FieldOptionSerializer(field_option_inst, data=field_option)
                        if fo_serializer.is_valid():
                            fo_serializer.save()
                        else:
                            transaction.savepoint_rollback(sp1)
                            return Response(fo_serializer.data, status=status.HTTP_400_BAD_REQUEST)
                else:
                    transaction.savepoint_rollback(sp1)
                    return Response(ft_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            transaction.savepoint_commit(sp1)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        risk_type = self.get_risk_type(pk)
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
