from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='jimbo', email='jimbo@email.com', password='testpass123'
        )
        self.assertEqual(user.username, 'jimbo')
        self.assertEqual(user.email, 'jimbo@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)