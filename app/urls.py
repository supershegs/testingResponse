from django.urls import path
from .views import ResponseView




urlpatterns = [
    path('grade', ResponseView.as_view()),   
]