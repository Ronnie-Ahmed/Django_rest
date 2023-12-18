from rest_framework import serializers
from .models import Snippets

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Snippets
        fields=('title','name','rmail')