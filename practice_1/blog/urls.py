from django.urls import path
from .views import ListPost, DetailPost

urlpatterns = [
    path('post/', ListPost.as_view(), name='list_post'),
    path('post/<int:pk>/', DetailPost.as_view(), name='detail_post'),
]
