from django.contrib.auth import get_user_model
from products.models import Product
from django.test import TestCase

User = get_user_model

class ProductTestCase(TestCase):

    def setUp(self):
        user1 =  User(email="saul@saul.com")
        user1.is_staff = True
        user1.set_password("saul")
        user1.save()
