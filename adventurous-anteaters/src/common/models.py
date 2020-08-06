from django.db import models
from django.utils import timezone


# we use save because auto_now is evil (https://stackoverflow.com/a/1737078)
class BaseModel(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, **kwargs)
