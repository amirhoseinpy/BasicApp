from django.views import generic
from django.urls import reverse_lazy

from .models import SimpleThing
from .forms import SimpleThingForm


class SimpleThingView(generic.CreateView):
    model = SimpleThing
    form_class = SimpleThingForm
    template_name = 'simple_thing.html'
    success_url = reverse_lazy('requested_app:simple_thing')
