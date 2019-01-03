from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import mixins, generics, permissions

# Create your views here.

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  def perform_create(self, serializer):
      serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
