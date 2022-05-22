from .views import *

articles_list = APIArticlesViewSet.as_view({'get': 'list', 'post': 'create'})
article_details = APIArticlesViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})