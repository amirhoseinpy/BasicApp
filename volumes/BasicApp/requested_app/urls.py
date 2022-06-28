from django.urls import path

from .views import SimpleThingView

app_name = 'requested_app'
urlpatterns = [
    path('', SimpleThingView.as_view(), name='simple_thing'),
]
