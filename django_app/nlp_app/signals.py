from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FormSending, ByPass

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FormSending, ByPass

@receiver(post_save, sender=FormSending)
def create_bypass_for_formsending(sender, instance, created, **kwargs):
    if created:
        ByPass.objects.create(formsending=instance, status=False)
