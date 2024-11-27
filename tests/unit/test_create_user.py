import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_create_user():
    """
    Test unitaire pour vérifier la création d'un utilisateur.
    """
    user = User.objects.create_user(username='testuser', password='ValidPass123!')
    assert user.username == 'testuser'
    assert user.check_password('ValidPass123!')
