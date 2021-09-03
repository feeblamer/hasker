from index.models import Tag, User
from .parser import create_models_user

def add_users():
    users = create_models_user()
    for user in users:
        u = User.objects.create(
            username=user.username,
            email=user.email,
        )
        u.set_password(user.password)

def add_tags(words:list):
    for word in words:
        Tag.objects.create(word=word)
    print('Доавленфы теги')