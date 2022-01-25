from django.urls import path

from .views import ListPostsView, DetailPostView, CreatePostView, DeletePostView

urlpatterns = [
    path("", ListPostsView.as_view(), name="list-posts"),
    path("<int:post_id>/", DetailPostView.as_view(), name="post-detail"),
    path("create/", CreatePostView.as_view(), name="create-post"),
    path("delete/<int:post_id>/", DeletePostView.as_view(), name="delete-post")
]
