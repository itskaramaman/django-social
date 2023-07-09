"""Views for Blog"""
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Blog
from blog.serializers import BlogSerializer


class BlogList(generics.ListCreateAPIView):
    """
    Get blogs lists or add a blog
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get a blog, update it or delete it
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer