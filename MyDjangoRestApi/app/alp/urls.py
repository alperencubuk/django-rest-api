from django.urls import path
from app.alp import views

urlpatterns = [
    path('', views.UserView.as_view()),
]