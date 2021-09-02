import index.Question as Question
import index.User as User
import index.Tag as Tag
from random import randint
from bs4 import BeautifulSoup
import requests

def add_tag_to_db(word):
    pass

def get_html(url):
    r = requests.get(url)
    return r.text

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', {'class':'structItemContainer-group js-threadList'})
    print(div)


def add_question_to_db(title, content):
    q =  Question.objects.create(
            title=title,
            content=content,
            author=User.objects.all()[randint(0, 5)], 
            )
    q.tags.add(Tad.objects.all()[randint(1,38)])
    q.tags.add(Tad.objects.all()[randint(1,38)])
    q.tags.add(Tad.objects.all()[randint(1,38)])
            
    


if __name__ == "__main__":
    print('jhkjhksd')    

