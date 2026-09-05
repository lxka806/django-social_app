from django.shortcuts import get_object_or_404, render, redirect

from .utils import (
    register as register_user,
    login as login_user,
    get_user_info,
    get_all_users,
    get_current_user,
    logout as logout_user
)

from .forms import registerForm, LoginForm
from .models import User

def all_users(req):
    context = {
        "all_users": get_all_users()
    }

    return render(req, "all_users.html", context)


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
    user_id = req.GET.get("user_id")
    if user_id:
        user = get_object_or_404(User, id=user_id)
    else:
        try:
            user = get_current_user()
        except User.DoesNotExist:
            return redirect("login_user")

    context = {
        "user": user
    }

    return render(req, "profile.html", context)


def logout(req):
    logout_user()
    return redirect("login_user")

def user_info(req, id):
    user = get_user_info(id=id)
    context = {
        "user": user
    }
    return render(req, "users_details.html", context)