from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import UserBase

class NewUserForm(UserCreationForm):

    class Meta:
        model = UserBase
        fields = ("username", "email")


class UpdateUserForm(UserChangeForm):

    class Meta:
        model = UserBase
        fields = ("username", "email")