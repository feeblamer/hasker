from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from index.models import User, Answer, Question

class UserAdministrator(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email')}
        ),
    )


admin.site.register(User, UserAdministrator)
admin.site.register(Answer)
admin.site.register(Question)
