from .models import User


def register(req):
    new_user = User(
        username=req.get("username"),
        email=req.get("email"),
        password=req.get("password")
    )

    new_user.save()


def login(req):
    found_user = User.objects.filter(
        email=req.get("email"),
        password=req.get("password")
    ).first()

    if found_user is None:
        raise User.DoesNotExist

    User.objects.update(is_current_user=False)
    found_user.is_current_user = 1
    found_user.save()


def get_user_info(id):
    return User.objects.get(id=id)


def get_all_users():
    return User.objects.all()


def get_current_user():
    return User.objects.get(is_current_user=1)


def logout():
    current_user = get_current_user()
    current_user.is_current_user = 0
    current_user.save()