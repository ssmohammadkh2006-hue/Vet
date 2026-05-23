from django.db import models


class Product(models.Model):

    STATUS_CHOICES = [
    ('normal', 'عادي'),
    ('best_seller', 'الأكثر مبيعاً'),
    ('featured', 'مميز'),
    ]

    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to='products/')

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='normal'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ContactMessage(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Offer(models.Model):
    num_offer=models.IntegerField()