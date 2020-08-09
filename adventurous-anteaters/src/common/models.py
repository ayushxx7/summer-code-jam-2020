from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# we use save because auto_now is evil (https://stackoverflow.com/a/1737078)
class BaseModel(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class User(AbstractUser, BaseModel):
    username = None
    email = None
    is_staff = None
    date_joined = None
    login = models.CharField(
        _('login'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': _("A user with that login already exists."),
        },
    )

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.login
