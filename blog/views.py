"""Views for Blog"""
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Blog
from blog.serializers import BlogSerializer

@api_view(["GET", "POST"])
def blog_list(request):
    """
    Get all the blogs
    """
    if request.method == "GET":
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
