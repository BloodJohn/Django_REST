from rest_framework import viewsets
from django.utils import timezone
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer


class BlogList(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of posts.
    """
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = PostSerializer

    # возвращает json по http запросу
    def list(self, request, *args, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
