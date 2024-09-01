from django.db import models
from users.models import User
from loyalty.models import LoyaltyPoints
# Create your models here.
class Transaction(models.Model):
    """
    User transactions: purchases or actions for which points are awarded.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    loyalty_points = models.ForeignKey(LoyaltyPoints, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.created_at}"
