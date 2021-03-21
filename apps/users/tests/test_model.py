from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.users.models import CxUser

User = get_user_model()


class CxUserTest(TestCase):
    def test_user_model_customization(self):
        self.assertEqual(User, CxUser)
