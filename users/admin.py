from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'password')
