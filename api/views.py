from blogging.models import Post, Category
from rest_framework import viewsets
from api.serializers import PostSerializer, CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-published_date')
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
