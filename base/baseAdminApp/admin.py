from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import NewUserForm, UpdateUserForm
from .models import UserBase

class UserBaseAdmin(UserAdmin):
    add_form = NewUserForm
    form = UpdateUserForm
    model = UserBase
    list_display = ["email", "username",]

admin.site.register(UserBase, UserBaseAdmin)
