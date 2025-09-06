from django.db import models

class Patient(models.Model):
    iin = models.CharField(max_length=12,  blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="visits")
    date = models.DateField()
    doctor = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def payment_status(self):
        return "Оплачено" if self.is_paid else "Не оплачено"

