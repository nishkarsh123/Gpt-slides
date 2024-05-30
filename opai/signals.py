from django.dispatch import receiver
from django.db.models.signals import post_save
from .tasks import send_generation_request_to_GPT_task
import uuid
from .models import PPT


@receiver(post_save, sender=PPT) 
def save_slides(sender, instance, created, **kwargs):
    if created:
        send_generation_request_to_GPT_task.delay(instance.id)
    # unique_filename = f"{uuid.uuid4()}.pptx"
    # unique_file_path = MEDIA_ROOT/ "ppt" /f"{unique_filename}"