from django.contrib.auth import get_user_model
from django.test import TestCase

from products.models import Product

User = get_user_model()

class ProductTestCase(TestCase):

    def setUp(self):
        staff_user =  User(email="saul@saul.com", username="saul")
        staff_user.set_password("saul")
        staff_user.is_staff = True
        staff_user.is_superuser = True
        staff_user.save()

        non_staff_user =  User(email="ceci@ceci.com", username="ceci")
        non_staff_user.is_staff = False
        non_staff_user.is_superuser = False
        non_staff_user.set_password("ceci")
        non_staff_user.save()

    def test_user_create(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_negative_product_create_permission(self):
        url = '/products/create/'
        data = {
            'product_name': 'Fruity Pebbles',
            'price': 3,

        }
        self.client.login(username='ceci', password='ceci')
        response = self.client.post(url, data)
        self.assertNotEqual(response.status_code, 200)
        
    def test_product_create_permission(self):
        url = '/products/create/'
        data = {
            'product_name': 'Fruity Pebbles',
            'price': 3,

        }
        self.client.login(username='saul', password='saul')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200) 

