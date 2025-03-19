from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
    path('test/', views.test, name='test'),
    path('register/', views.register, name='register')
]