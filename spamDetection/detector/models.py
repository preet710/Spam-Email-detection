from django.db import models

# Create your models here.
# detector/models.py
from django.db import models

class SpamDetectionModel(models.Model):
    content = models.TextField()
    result = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content[:50]} - {self.result}"
