from index.models import Tag, User, Question
from .parser import create_models_user, create_models_question
from random import choice, sample


def add_users():
    users = create_models_user()
    for user in users:
        u = User.objects.create(
            username=user.username,
            email=user.email,
        )
        u.set_password(user.password)

def add_questions():
    questions = create_models_question()
    for question in questions:
        q = Question.objects.create(
                title=question.title,
                content=question.content,
                author=User.objects.all()[choice(range(0,6))],
               )

        q.tags.add(Tag.objects.all()[question.tags[0]])
        q.tags.add(Tag.objects.all()[question.tags[1]])
        q.tags.add(Tag.objects.all()[question.tags[2]])                       
                

def add_tags(words:list):
    for word in words:
        Tag.objects.create(word=word)
    print('Доавленфы теги')
