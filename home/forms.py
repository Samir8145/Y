from django.forms import ModelForm
from .models import Contact

class ModelContact(ModelForm):
    class Meta:
        model = Contact
        exclude = ['created']
