from django.forms import ModelForm
from requested_app.models import SimpleThing


class SimpleThingForm(ModelForm):
    class Meta:
        model = SimpleThing
        fields = [
            'name',
            'family',
            'phone_number',
        ]
