from django.contrib import admin
from django.urls import path, include

from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', Students.as_view()),
    path('post/create/', CreateStudent.as_view()),
    path('post/delete', DestroyStudent.as_view()),
    path('comment/list', CommentList.as_view()),
    path('comment/create', Createcomment.as_view()),
    path('comment/delete', Destroycomment.as_view()),
    path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.jwt')),
]
