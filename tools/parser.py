from collections import namedtuple
from random import sample, choice
from bs4 import BeautifulSoup
import requests
import json
import string
BASE_URL = 'https://discuss.python.org/c/users/7.json?page={}'
BASE_POST_URL = 'https://discuss.python.org/t/{}/{}'

User = namedtuple('User', ['username', 'password', 'email'])
Question = namedtuple('Question', ['title', 'content', 'tags'])

def grab_usernames(url):
    j = get_json(url)
    users = get_users(j)
    return [user['username'] for user in users]


def email_generator():
    email_servers = [
        'mail.ru',
        'hotmail.ru',
        'top.org',
        'yandex.ru',
    ]
    symbols = string.ascii_lowercase
    adress = ''.join(sample(symbols, 6))
    email = '@'.join(
        [
            adress,
            choice(email_servers)
        ]
    )
    return email


def password_generator():
    symbols = '{}{}{}'.format(
        string.ascii_lowercase,
        string.digits,
        string.ascii_uppercase,
    )
    password = ''.join(sample(symbols, 8))
    return password

def get_username(user):
    return user['username']

def get_json(url):
    r = requests.get(url)
    return r.json()

def get_topics(url):
    j = get_json(url)
    return  j['topic_list']['topics']

def get_users(j):
    return j['users']

def create_models_user():
    users = []
    for i in range(1, 3):
        url = BASE_URL.format(i)
        usernames = grab_usernames(url)
        for username in usernames:
            user = User(
                username,
                password_generator(),
                email_generator(),
            )
            users.append(user)
    return users

def grub_article(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    post = soup.find('div', class_='post')
    if post:
        text = ''
        for tag in post.children:
            try:
                text += tag.text
            except:
                print('Найден тег без текста')
        return text
    else:
        raise Exception('Не удалось найти содержимое поста')
    

def url_for_grub(page=6):
    topics = get_topics(BASE_URL.format(page))
    number = choice(range(0,20))
    slug = topics[number]['slug']
    post_id = topics[number]['id']
    return BASE_POST_URL.format(slug, post_id)


def create_models_question():
    questions = []
    for i in range(1,2):
        url = BASE_URL.format(i)
        topics = get_topics(url) 
        for topic in topics:
            slug = topic['slug']
            title = topic['title']
            post_id = topic['id']
            url_post = BASE_POST_URL.format(slug, post_id)
            content = grub_article(url_post)
            tags = sample(range(0,10), 3)
            questions.append(
                Question(title, content, tags)
                )
    return questions
    


def main():
    pass


if __name__ == '__main__':
    main()
