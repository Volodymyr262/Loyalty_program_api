from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings


class LoyaltyLevel(models.Model):
    """
    Loyalty levels, such as "Silver", "Gold", "Platinum".
    """
    name = models.CharField(max_length=50)
    min_points = models.PositiveIntegerField(default=0)
    benefits = models.TextField(help_text="Description of the level's benefits")

    class Meta:
        verbose_name = "Loyalty Level"
        verbose_name_plural = "Loyalty Levels"

    def __str__(self):
        return self.name


class LoyaltyStatus(models.Model):
    """
    The user's loyalty status: how many points they've accumulated and their corresponding level.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    points = models.PositiveIntegerField(default=0, db_index=True)
    level = models.ForeignKey(LoyaltyLevel, on_delete=models.SET_NULL, null=True)
    rewards = ArrayField(models.CharField(max_length=100), blank=True, default=list)

    class Meta:
        verbose_name = "Loyalty Status"
        verbose_name_plural = "Loyalty Statuses"

    def __str__(self):
        return f"{self.user.username} - {self.points} points"


class LoyaltyPoints(models.Model):
    """
    A log of point transactions, recording point accruals for the user.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points = models.IntegerField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Loyalty Points"
        verbose_name_plural = "Loyalty Points"

    def __str__(self):
        return f"{self.user.username} - {self.points} points"


class PointsAllocationRule(models.Model):
    """
    Rules for point allocation: how many points to award for specific actions.
    """
    description = models.CharField(max_length=255)
    points_per_unit = models.PositiveIntegerField()
    applicable_to = models.CharField(max_length=100, help_text="Conditions under which the rule applies")

    class Meta:
        verbose_name = "Points Allocation Rule"
        verbose_name_plural = "Points Allocation Rules"

    def __str__(self):
        return f"{self.description} - {self.points_per_unit} points per {self.applicable_to}"
