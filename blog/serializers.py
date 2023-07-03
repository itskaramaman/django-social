from rest_framework import serializers
from blog.models import Blog


class BlogSerializer(serializers.Serializer):
    """
    Serializer for Blog
    """
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'author', 'created_at', 'updated_ad']
