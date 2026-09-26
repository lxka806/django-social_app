from django.shortcuts import get_object_or_404, redirect, render

from .utils import add_post, get_all_posts
from .forms import AddPost
from .models import Post

from users.models import User
from users.utils import get_current_user

def all_posts(req):
    try:
        current_user = get_current_user()
    except User.DoesNotExist:
        current_user = None

    context = {
        "all_posts": get_all_posts().select_related("user"),
        "current_user": current_user,
    }

    return render(req, "all_posts.html", context)


def add_posts(req):
    try:
        get_current_user()
    except User.DoesNotExist:
        return redirect("login_user")

    form = AddPost(req.POST or None)
    if req.method == "POST":
        if form.is_valid():
            add_post(form.cleaned_data)
            return redirect("all_posts")

    context = {
        "form": form,
        "current_user": get_current_user(),
    }

    return render(req, "add_posts.html", context)


def like_post(req, post_id):
    post = get_object_or_404(Post, id=post_id)
    try:
        user = get_current_user()
    except User.DoesNotExist:
        return redirect("login_user")

    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect("all_posts")

def delete_post(req, post_id):
    post = get_object_or_404(Post, id=post_id)

    if req.method == "POST":
        post.delete()
    
    return redirect("all_posts")