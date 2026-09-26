from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from .utils import register as register_user, login as login_user, get_current_user, logout as logout_user

from .forms import registerForm, LoginForm
from .models import User

def register(req):
    if req.method == "POST":
        register_user(req.POST)
        return redirect("login_user")

    context = {
        'context': registerForm()
    }

    return render(req, "register.html", context)


def login(req):
    context = {
        "errors": []
    }

    if req.method == "POST":
        try:
            login_user(req.POST)
            return redirect("profile_user")
        except:
            context["errors"].append("Invalid email or password")

    login_form = {
        'context': LoginForm()
    }

    return render(req, "login.html", login_form)


def get_profile(req):
    try:
        user = get_current_user()
    except User.DoesNotExist:
        return redirect("login_user")

    context = {
        "user": user,
        "current_user": user,
        "posts": user.posts.all(),
        "post_count": user.posts.count(),
    }

    return render(req, "profile.html", context)


def logout(req):
    logout_user()
    return redirect("login_user")


def user_info(req, id):
    user = get_object_or_404(User, id=id)
    try:
        current_user = get_current_user()
    except User.DoesNotExist:
        current_user = None

    return render(req, "users_details.html", {
        "user": user,
        "current_user": current_user,
        "posts": user.posts.all(),
    })
