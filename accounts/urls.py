from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.registeraion_page, name='register')
]