from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    privilege_level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    run = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.ForeignKey("Role", on_delete=models.PROTECT, related_name="profiles")

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.run}"
    
