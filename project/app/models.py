from django.db import models

class details(models.Model):
    name = models.CharField(max_length=100, default="Default Name")  # Default value for name
    email = models.EmailField(unique=True, default="default@example.com")  # Default email
    password = models.CharField(max_length=128, default="defaultpassword")  # Default password

    def __str__(self):
        return self.name

