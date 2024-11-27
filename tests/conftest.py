import os
import django
from django.conf import settings
import pytest
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_blog.settings')
django.setup()

@pytest.fixture
def create_test_user(db):
    return User.objects.create_user(
        username="testuser",
        password="ValidPass123!",
        is_staff=True,  # Permet d'accéder au panneau admin
    )
