from cgitb import lookup
from dataclasses import field
from rest_framework import serializers
from article.models import *


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'