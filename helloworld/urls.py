from django.urls import path

from . import views

app_name = 'helloworld'

urlpatterns = [
    path('fruits', views.index, name='index')
]
