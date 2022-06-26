from django.db import models
from userapp.models import Profile

# Create your models here.


class Transactions(models.Model):
    Tran_CHOICES = (
        ('Income', "income"),
        ('Expenses', "expenses"))
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(choices=Tran_CHOICES, max_length=10)

    def __str__(self):
        return str(self.user)
