from django.contrib import admin


# Register your models here.
from index.models import User, Question, Answer

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)

