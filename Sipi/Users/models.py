from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Meta:
        ordering = ["-date_joined"]

    # fields
    avatar = models.ImageField(
        _("Аватар"), upload_to="avatars/", default="avatars/default.png"
    )

    # def get_absolute_url(self):
    #     return reverse("dashboard:index", kwargs={"username": self.username})

