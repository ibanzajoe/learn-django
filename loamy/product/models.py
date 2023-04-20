from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128, blank=True)
    
    def __str__(self) -> str:
        return self.name