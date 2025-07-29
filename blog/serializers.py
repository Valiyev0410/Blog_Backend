from rest_framework import serializers
from .models import *

class PostSerializers(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = "__all__"

class CommentSerializers(serializers.ModelSerializer):
    class Meta():
        model = Comment
        fields = "__all__"
