
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from .utils import (
    register as register_user,
    login as login_user,
    get_current_user,
    logout as logout_user,
)
from .forms import registerForm, LoginForm
from .models import User
import random


def register(req):
    form = registerForm()

    if req.method == "POST":
        form = registerForm(req.POST)

        if form.is_valid():
            verification_code = ""
            alp = "abcdefghijklmnopqrstuvwxyz123456789"

            for i in range(6):
                verification_code += alp[random.randint(0, len(alp) - 1)]

            req.session["verification_code"] = verification_code
            req.session["registration_data"] = form.cleaned_data

            email = form.cleaned_data["email"]

            send_mail(
                "Verify your account",
                f"Your verification code is: {verification_code}",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            return redirect("verification")

    return render(req, "register.html", {"context": form})


def verify_user(req):
    error = ""

    if req.method == "POST":
        entered_code = req.POST.get("verification_code", "")
        saved_code = req.session.get("verification_code")

        if saved_code and entered_code == saved_code:
            registration_data = req.session.get("registration_data")

            if registration_data:
                register_user(registration_data)

                del req.session["verification_code"]
                del req.session["registration_data"]

                return redirect("login_user")

            error = "Registration data not found. Please register again."
        else:
            error = "Invalid verification code."

    return render(req, "user_verification.html", {"error": error})

def login(req):
    context = {"errors": []}

    if req.method == "POST":
        try:
            login_user(req.POST)
            return redirect("profile_user")
        except Exception:
            context["errors"].append("Invalid email or password")

    context["context"] = LoginForm()

    return render(req, "login.html", context)



def get_profile(req):
    try:
        user = get_current_user()
    except User.DoesNotExist:
        return redirect("login_user")

    if req.method == "POST":
        image = req.FILES.get("image")

        if image:
            user.avatar = image
            user.save()

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

    return render(
        req,
        "users_details.html",
        {
            "user": user,
            "current_user": current_user,
            "posts": user.posts.all(),
        },
    )
