from django.db import models

from django.db import models

class Ping(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)