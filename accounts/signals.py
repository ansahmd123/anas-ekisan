from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin import widgets

@receiver(post_save, sender=User)
def create_new_user_notification(sender, instance, created, **kwargs):
    if created: 
        message = f"A new user has been created: {instance.name} ({instance.email})"
        request = kwargs.get('request')  
        if request is not None:
            from django.contrib.messages import info  
            info(request, message, extra_tags='new_user')  
        else:
            print(message) 
