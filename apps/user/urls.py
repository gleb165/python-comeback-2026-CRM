from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('hello-view', views.HelloView.as_view()),
]