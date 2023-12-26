from django.urls import path
from users.views import HomePage, LoginView, RegisterView

urlpatterns = [
    
    path('', HomePage, name='homepage'),
    path('login/', LoginView, name='login'),
    path('register/', RegisterView, name='register'),
]