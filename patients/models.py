from django.db import models

# Create your models here.
from django.conf import settings
# from django.contrib.auth.models import User

class Patient(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name