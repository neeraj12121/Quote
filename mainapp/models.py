from django.db import models

class Quote(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='quotes')

    class Meta:
        ordering = ('-created',)

