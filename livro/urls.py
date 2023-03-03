from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('visualiza/<int:id>', views.visualiza, name='visualiza')
]
