from django.urls import path
from blog.views import BlogList, BlogDetail


urlpatterns = [
    path("", BlogList.as_view(), name="blog-list"),
    path("<int:pk>/", BlogDetail.as_view(), name="blog-detail"),
]
