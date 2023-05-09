from allauth.account.forms import SignupForm
from django import forms
from django.contrib import messages
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserSignupForm(SignupForm):
    """Форма регистрации пользователя"""

    name = forms.CharField(
        max_length=30,
        label=_("Имя"),
        widget=TextInput(attrs={"placeholder": _("First Name")}),
    )

    field_order = [
        "first_name",
        "password1",
        "username",
        "password2",
        "email",
    ]

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request", None)

        super().__init__(*args, **kwargs)

        self.fields["email"].label = "Email"
        self.fields["email"].required = True
        self.fields["email"].widget.attrs.update({"placeholder": "mail@gmail.com"})

        self.fields["username"].label = "Login"
        self.fields["username"].widget.attrs.update({"placeholder": "Login"})

        self.fields["password1"].label = _("Пароль")
        self.fields["password1"].widget.attrs.update({"placeholder": "*********"})

        self.fields["password2"].label = _("Повторите пароль")
        self.fields["password2"].widget.attrs.update({"placeholder": "*********"})

    def save(self, request):
        user = super().save(request)
        if user:
            user.save()
        return user
