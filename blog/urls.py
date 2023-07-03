from django.urls import path
from blog.views import blog_list


urlpatterns = [
    path("", blog_list, name="blog-list")
]
