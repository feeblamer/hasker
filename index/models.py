from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    nickname = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d')
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nickname

class Tag(models.Model):
    word = models.CharField(max_length=20)

class Question(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User , on_delete=models.CASCADE,)
    create_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

class Answer(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    write_date = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField()
