
from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.index, name = 'index'),
    path('detail/<int:pk>/', views.detail, name = 'detail'),
    path('create/',views.create, name = 'create'),
    path("<int:pk>/edit", views.edit, name="edit"),
    path("<int:pk>/update", views.update, name = "update"),
    path('<int:pk>/del_post', views.del_post, name = 'del_post'),


]
