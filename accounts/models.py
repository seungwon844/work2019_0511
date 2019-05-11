from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    # email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)

    def get_absolute_url(self):
        return ('http://127.0.0.1:8000/')
