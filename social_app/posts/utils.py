from .models import Post, Comment
from users.utils import get_current_user

def add_post(req):
    if req.get("post_image"):
        new_post = Post(
            title=req.get("title"),
            content=req.get("content"),
            user=get_current_user(),
            post_image=req.get("post_image")
        )
    else:
        new_post = Post(
            title=req.get("title"),
            content=req.get("content"),
            user=get_current_user(),
        )

    new_post.save()

    return new_post

def get_all_posts():
    return Post.objects.all()
