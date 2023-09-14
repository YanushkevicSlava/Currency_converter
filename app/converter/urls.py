from django.urls import path
from .views import converter_index


app_name = 'converter'

urlpatterns = [
    path('', converter_index),
]