from rest_framework import viewsets
from django.utils import timezone

from blog.models import Post
from blog.serializers import PostSerializer


class BlogList(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of posts.
    """
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = PostSerializer