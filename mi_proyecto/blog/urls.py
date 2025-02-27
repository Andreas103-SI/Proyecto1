from django.urls import path
from .views import (
    hola_mundo, PostListView, PostDetailView, 
    PostCreateView, PostUpdateView, PostDeleteView, PostAPIView
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Ruta para la API (asegúrate de que si usas esta ruta, no entre en conflicto con otras)
    path('api/posts/', PostAPIView.as_view(), name='post_api'),

    # Rutas de la aplicación
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Rutas de autenticación
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Ruta adicional si la necesitas
    path('hola/', hola_mundo, name='hola_mundo'),
]

