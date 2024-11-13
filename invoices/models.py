from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=10, unique=True)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.invoice_number} - {self.customer_name}"

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        related_name='details',
        on_delete=models.CASCADE
    )
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    line_total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.line_total = self.quantity * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.invoice.invoice_number} - {self.description}"