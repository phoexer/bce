from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from bce.models import RiskType
from django.contrib.auth.models import User
import json


class RiskTypeTests(APITestCase):

    def setUp(self):
        if User.objects.count() == 0:
            self.user = User.objects.create_user('testuser', 'password')
        assert(User.objects.count() == 1)
        self.client.force_authenticate(self.user)

    def create_risk_type(self):
        """
        Ensure we can create a new risk type.
        """
        url = reverse('risk-type-list')

        count = RiskType.objects.count()

        with open('./td/risktype_l3.json') as f3:
            data = json.load(f3)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RiskType.objects.count(), count + 1)
        self.assertEqual(RiskType.objects.get().name, 'Auto-Insurance')
        return response.json()

    def get_list(self):
        url = reverse('risk-type-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.json()

    def test_create_with_bad_json(self):
        """
        Testing the badly formated json files
        """
        url = reverse('risk-type-list')

        count = RiskType.objects.count()

        with open('./td/risktype_l3_err1.json') as f1:
            data1 = json.load(f1)

        with open('./td/risktype_l3_err2.json') as f2:
            data2 = json.load(f2)

        response = self.client.post(url, data1, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(RiskType.objects.count(), count)

        response = self.client.post(url, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(RiskType.objects.count(), count)

    def get_risktype(self, id):
        get_url = reverse('risk-type-detail', kwargs={'pk': id})

        response = self.client.get(get_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.json()

    def edit_risktype(self, id, data):
        url = reverse('risk-type-detail', kwargs={'pk': id})

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def delete_risktype(self, id):
        url = reverse('risk-type-detail', kwargs={'pk': id})

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_risktype_crud(self):
        """
        Tests the crudiness of risk type
        """
        count = RiskType.objects.count()

        # list_url = reverse('risk-type-list')
        risk_type = self.create_risk_type()

        id = risk_type['id']

        rt_list = self.get_list()

        assert(len(rt_list) == count + 1)

        risk_type = self.get_risktype(id)

        s = 'This is a new Label'

        assert(risk_type['label'] != s)

        risk_type['label'] = s

        self.edit_risktype(id, risk_type)

        risk_type = []

        risk_type = self.get_risktype(id)

        assert(risk_type['label'] == s)

        self.delete_risktype(id)


class AccessTests(APITestCase):

    def setUp(self):
        if User.objects.count() == 0:
            self.user = User.objects.create_user('testuser', 'password')

        assert(User.objects.count() == 1)

    def test_create_risk_type(self):
        """
        Should not create
        """
        url = reverse('risk-type-list')

        count = RiskType.objects.count()

        with open('./td/risktype_l3.json') as f3:
            data = json.load(f3)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(RiskType.objects.count(), count)

    def test_list(self):
        url = reverse('risk-type-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
