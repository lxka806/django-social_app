from .models import Post
from users.utils import get_current_user

def add_post(req):
    new_post = Post(
        title=req.get("title"),
        content=req.get("content"),
        user=get_current_user()
    )

    new_post.save()

    return new_post

def get_all_posts():
    return Post.objects.all()