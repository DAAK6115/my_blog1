import pytest
from django.contrib.auth.forms import UserCreationForm

@pytest.mark.django_db
def test_user_creation_form_valid_data():
    """
    Test unitaire pour valider le formulaire d'inscription avec des données valides.
    """
    form = UserCreationForm(data={
        'username': 'testuser',
        'password1': 'ValidPass123!',
        'password2': 'ValidPass123!',
    })
    assert form.is_valid()
