from django.urls import path
from .views import DateConverterView

urlpatterns = [
    path('converter', DateConverterView.as_view(), name='date_converter'),
    ]
