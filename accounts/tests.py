from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

User = get_user_model()

class UserTestCase(TestCase):
    
    def setUp(self):
        user1 =  User(username="saul")
        user1.is_staff = True
        user1.is_superuser = True
        user1.set_password("saul")
        user1.save()

    def test_user_create(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1) 