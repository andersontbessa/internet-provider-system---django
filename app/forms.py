from django.forms import ModelForm
from app.models import Animals

class AnimalsForm(ModelForm):
    class Meta:
        model = Animals
        fields = ['nome', 'birthDate', 'cpf', 'address', 'contact']
        
