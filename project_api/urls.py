from django.urls import path, include
from .router import *

urlpatterns = [

    # Entrypoint/Root (Endpoint) for api
    path('', include(default_router.urls)),
]