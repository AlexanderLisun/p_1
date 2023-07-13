from django.urls import path
from .views import index1

urlpatterns = [
    path('lesson_4', index1)
]