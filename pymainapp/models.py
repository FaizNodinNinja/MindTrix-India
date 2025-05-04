from django.db import models

# Create your models here.

from django.db import models

class Service(models.Model):  # ✅ Dynamic Service Model
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # ✅ ForeignKey for Dynamic Choice
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"

