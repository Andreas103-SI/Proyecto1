from django.urls import path
from .views import hola_mundo, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostAPIView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),  # Lista de posts en la página principal
    # path('hola/', hola_mundo, name='hola_mundo'),  # Comentado o eliminado
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Detalles de un post específico
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # Crear un nuevo post
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),  # Editar un post existente
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Eliminar un post
    path('login/', LoginView.as_view(), name='login'),  # Página de inicio de sesión
    path('logout/', LogoutView.as_view(), name='logout'),  # Página de cierre de sesión
    path('api/posts/', PostAPIView.as_view(), name='post_api'),  # API para obtener posts
]

