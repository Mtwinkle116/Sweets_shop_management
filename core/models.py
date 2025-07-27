from django.contrib.auth.models import AbstractUser
from django.db import models

class Sweet(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    purchased_sweets = models.ManyToManyField(Sweet, through='Purchase')        

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    sweet = models.ForeignKey(Sweet, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} purchased {self.quantity} of {self.sweet.name}"

