from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    college = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    player_number = models.PositiveIntegerField(unique=True, blank=True, null=True)  # Allow null for initial migration

    def save(self, *args, **kwargs):
        if self.player_number is None:  # Auto-generate player number only if missing
            last_player = Registration.objects.order_by('-player_number').first()
            self.player_number = (last_player.player_number + 1) if last_player else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Player {self.player_number:03}: {self.name}"
