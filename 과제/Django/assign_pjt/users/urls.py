from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "users"

urlpatterns = [    
    path('login/', views.login, name = 'login'),
    path("logout/", views.logout, name='logout'),    
    path('signup/', views.signup, name = 'signup'),
    path("delete/", views.delete, name='delete'),
    path('profile/', views.profile, name = 'profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('update/', views.update, name="update"),
    path("passward/", views.change_passward, name = "change_passward"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)