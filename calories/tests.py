from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_entry(self):
        url = '/api/entries/'
        data = {
            'date': '2023-06-15',
            'time': '12:00:00',
            'text': 'Sample entry',
            'calories': 500
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], self.user.id)
        self.assertEqual(response.data['date'], '2023-06-15')
        self.assertEqual(response.data['time'], '12:00:00')
        self.assertEqual(response.data['text'], 'Sample entry')
        self.assertEqual(response.data['calories'], 500)

    def test_retrieve_entry(self):
        entry = self.user.entry_set.create(
            date='2023-06-15',
            time='12:00:00',
            text='Sample entry',
            calories=500
        )
        url = f'/api/entries/{entry.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], self.user.id)
        self.assertEqual(response.data['date'], '2023-06-15')
        self.assertEqual(response.data['time'], '12:00:00')
        self.assertEqual(response.data['text'], 'Sample entry')
        self.assertEqual(response.data['calories'], 500)

    def test_update_entry(self):
        entry = self.user.entry_set.create(
            date='2023-06-15',
            time='12:00:00',
            text='Sample entry',
            calories=500
        )
        url = f'/api/entries/{entry.id}/'
        data = {
            'date': '2023-06-16',
            'time': '13:00:00',
            'text': 'Updated entry',
            'calories': 600
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], self.user.id)
        self.assertEqual(response.data['date'], '2023-06-16')
        self.assertEqual(response.data['time'], '13:00:00')
        self.assertEqual(response.data['text'], 'Updated entry')
        self.assertEqual(response.data['calories'], 600)

    def test_delete_entry(self):
        entry = self.user.entry_set.create(
            date='2023-06-15',
            time='12:00:00',
            text='Sample entry',
            calories=500
        )
        url = f'/api/entries/{entry.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(self.user.entry_set.filter(id=entry.id).exists())
