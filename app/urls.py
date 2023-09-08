from django.urls import path
from .views import ResponseView




urlpatterns = [
    path('api', ResponseView.as_view()),   
]