from django.db import models
from django.urls import reverse




class Product(models.Model):
    name = models.CharField(max_length=100) # название
    price = models.CharField(max_length=100) # цена
    description = models.TextField(blank=True) # описание (необязательно)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_id': self.id})
    
