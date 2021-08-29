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

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['reg_date', 'nickname', 'email']

class Tag(models.Model):
    word = models.CharField(max_length=20)

    def __str__(self):
        return self.word

class Question(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    create_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ['create_date']

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    write_date = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField()
    
    def __str__(self):
        return self.question.title + self.content

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ['write_date']
