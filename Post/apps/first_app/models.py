from __future__ import unicode_literals
from django.db import models
class note(models.Model):
    message = models.CharField(max_length = 2000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)