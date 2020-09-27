from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('factorial/', views.factorial, name='factorial'),
    path('conversion/', views.conversion, name='conversion'),
    path('fibonacci/', views.fibonacci, name='fibonacci'),
    path('exponent/', views.exponent, name='exponent'),
    path('quadratic/', views.quadratic, name='quadratic'),
    path('pythagorean/', views.pythagorean, name='pythagorean'),
]