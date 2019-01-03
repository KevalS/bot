from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('pk', 'author', 'title', 'text', 'created_date')
    read_only_fields = ('author','created_date', 'published_date')
