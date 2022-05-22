from rest_framework import routers
from .viewsets import *

default_router = routers.DefaultRouter()
default_router.register(r'articles', APIArticlesViewSet)