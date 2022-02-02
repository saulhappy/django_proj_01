from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

User = get_user_model()

class UserTestCase(TestCase):
    
    def setUp(self):
        user1 =  User(email="saul@saul.com")
        user1.is_staff = True
        user1.is_superuser = True
        user1.set_password("saul")
        user1.save()

    def test_user_create(self):
        user_count = User.objects.all().count()
        user_qs = User.objects.filter(email__iexact="saul@saul.com")
        user_exists = user_qs.exists()
        self.assertTrue(user_exists)
        self.assertEqual(user_count, 1) 