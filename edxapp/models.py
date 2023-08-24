from django.db import models
from django.contrib.auth import get_user_model


class TrackedModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Created_At', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(verbose_name='Updated_At', auto_now=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Greeting(TrackedModel):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
