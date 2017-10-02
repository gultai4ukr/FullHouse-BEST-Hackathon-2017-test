from django.core.validators import MaxLengthValidator
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(validators=[MaxLengthValidator(10000)])

    class Meta:
        ordering = ['-id']
