from django.contrib import admin
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [    
    path('login/', views.login, name = 'login'),
    path("logout/", views.logout, name='logout'),    
    path('signup/', views.signup, name = 'signup'),
    path("delete/", views.delete, name='delete'),
    path('profile/', views.profile, name = 'profile'),
    path('update/', views.update, name="update"),
    path("passward/", views.change_passward, name = "change_passward"),
]
