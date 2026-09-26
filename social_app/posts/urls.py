from django.urls import path
from .views import add_posts, all_posts, like_post, delete_post, add_comment

urlpatterns = [
    path("", all_posts, name="all_posts"),
    path("add/", add_posts, name="add_posts"),
    path("delete/<int:post_id>/", delete_post, name="delete_post"),
    path("like/<int:post_id>/", like_post, name="like_post"),
    path("comment/<int:post_id>/", add_comment, name="add_comment")
]