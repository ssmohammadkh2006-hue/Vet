from django.contrib import admin
from .models import Product, ContactMessage, Offer


admin.site.register(Product)

admin.site.register(ContactMessage)

admin.site.register(Offer)
