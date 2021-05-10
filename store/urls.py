from django.urls import path
from store import views

urlpatterns = [
    path('login/', views.login_user)
]
