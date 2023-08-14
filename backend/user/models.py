from django.db import models
from investment.models import Investment
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,unique=True , on_delete=models.CASCADE, null=True, blank=True)
    invesments = models.ForeignKey(Investment, on_delete=models.CASCADE, null=True, blank=True)

    def clean(self, data) -> bool:
        if data.get("password") != data.get("password1"):
            raise ValidationError(_('Please make sure that the passwords in both fields are identical.'))
        return True