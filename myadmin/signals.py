# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.cache import cache

@receiver(post_save, sender=User)
def notify_new_farmer(sender, instance, created, **kwargs):
    if created and hasattr(instance, 'role') and instance.role == 'Farmer':  # Assuming 'role' is an attribute of User model
        message = f"New farmer added: {instance.name}"
        print(f"Signal triggered: {message}")
        # You can use Django's cache framework to store the notification message
        #cache.set('new_farmer_notification', message, timeout=60*60)  # Store for 1 hour
