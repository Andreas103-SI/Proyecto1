from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer

# Create your views here.
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("Hola Mundo")

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('post_list')  # Agregado success_url

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('post_list')  # Agregado success_url

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

class PostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)