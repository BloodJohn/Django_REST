from rest_framework import viewsets
from django.utils import timezone
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer


class BlogList(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of posts.
    """
    lookup_url_kwarg = 'post_id'
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = PostSerializer

    # возвращает json по http запросу
    def list(self, request, *args, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    # создает новую запись
    def create(self, request, *args, **kwargs):
        new_post = self.create(name="Joe")
        serializer = PostSerializer(new_post, many=False)
        return Response(serializer.data)

    # возвращает существующую запись
    def retrieve(self, request, *args, **kwargs):
        detail_post = self.get_object()
        return Response(detail_post.data)

    # частично обновляет существующую запись
    def partial_update(self, request, *args, **kwargs):
        update_post = self.get_object()
        update_post.update(name="Joe")
        update_post.save()
        return Response(update_post.data)

    # удаляет существующую запись
    def perform_destroy(self, instance):
        del_post = self.get_object()
        del_post.delete()
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
