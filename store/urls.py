from django.urls import path
from store import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('get/<str:site>', views.show_password, name='get_pssd'),
    path('add/', views.add_credentials, name='add'),
    path('edit/', views.edit_credentials, name='edit')
]
