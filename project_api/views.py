from .serializers import *
from rest_framework import permissions  # used to set permissions on api access
from .permissions import IsStaffOrNot  # custom permission for accessing api
from rest_framework import viewsets


class APIArticlesViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.order_by('-article_date')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)