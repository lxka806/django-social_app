
from django.shortcuts import render, redirect
from .models import Message
from users.models import User
from users.utils import get_current_user


def global_chat(req):
    try:
        current_user = get_current_user()
    except User.DoesNotExist:
        return redirect("login_user")

    if req.method == "POST":
        content = req.POST.get("content", "").strip()

        if content and len(content) <= 1000:
            Message.objects.create(
                user=current_user,
                content=content
            )

        return redirect("global_chat")

    messages = Message.objects.select_related("user").all()

    return render(req, "chat/global_chat.html", {
        "messages": messages,
        "current_user": current_user,
    })
