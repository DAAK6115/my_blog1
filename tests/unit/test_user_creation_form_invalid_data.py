import pytest
from django.contrib.auth.forms import UserCreationForm

@pytest.mark.django_db
def test_user_creation_form_invalid_data():
    """
    Test unitaire pour valider le formulaire d'inscription avec des mots de passe non concordants.
    """
    form = UserCreationForm(data={
        'username': 'testuser',
        'password1': 'ValidPass123!',
        'password2': 'InvalidPass123!',
    })
    assert not form.is_valid()
    assert 'password2' in form.errors
