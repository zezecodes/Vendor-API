from django.urls import path
from . import views

#URLconfig
urlpatterns = [
    path('hello/', views.say_hello)
]