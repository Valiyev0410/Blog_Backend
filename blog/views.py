from rest_framework import generics
from .serializers import *
from rest_framework.permissions import *


class Students(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [AllowAny]


class CreateStudent(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAdminUser]

class DestroyStudent(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAdminUser]



class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [AllowAny]


class Createcomment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [AllowAny]

class Destroycomment(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [IsAdminUser]
