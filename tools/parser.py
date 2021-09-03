from collections import namedtuple
from random import sample, choice

import requests
import json
import string
BASE_URL = 'https://discuss.python.org/c/users/7.json?page={}'

User = namedtuple('User', ['username', 'password', 'email'])

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

def get_topics(j):
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


def main():
    print(
        create_models_user()
    )

if __name__ == '__main__':
    main()
