from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Log(models.Model):
    payee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000000)
    quantity = models.DecimalField(max_digits=10000, decimal_places=2)
    fuel_type = models.CharField(max_length=100, choices=[
        ('petrol', 'petrol'), 
        ('cng', 'cng')], default='petrol', blank=False, null=False)
    odo = models.IntegerField(verbose_name="Odometer Reading")
    location = models.CharField('Location of Petrol pump', max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def unit(self):
        return 'ls' if self.fuel_type == "petrol" else 'kgs'

    def is_editable(self):
        current_time = timezone.now()
        time_elased = 60
        delta = current_time - self.created_at
        delta_in_minutes = delta.total_seconds() / 60
        return delta_in_minutes <= time_elased

    def __str__(self):
        return f'{self.quantity} {self.fuel_type}'

