
from datetime import datetime
from celery import shared_task
from .utils import send_generation_request_to_gpt
from .models import PPT
from pptx import Presentation	 
from pptx.enum.shapes import MSO_SHAPE_TYPE
from rest_framework.response import Response
from django.conf import settings
 

MEDIA_ROOT=settings.MEDIA_ROOT

def find_shape_by_text(shapes, text):
    for shape in shapes:
        if shape.has_text_frame:
            if shape.text.lower() == text.lower():
                return shape
        elif shape.shape_type == MSO_SHAPE_TYPE.GROUP:
            return find_shape_by_text(shape.shapes, text)
    return None
@shared_task
def send_generation_request_to_GPT_task(unique_filename, id):
    unique_file_path = MEDIA_ROOT/ "ppt" /f"{unique_filename}"
    # with open (unique_file_path, "rb") as file:
    new_ppt = PPT.objects.filter(id=id).first()
    try:
        result = send_generation_request_to_gpt()
        if result:
            root = Presentation(unique_file_path)
            slide = root.slides[0]  # considering only the first slide
            title = find_shape_by_text(slide.shapes, "THOUGHT/JOKE/QUOTE OF THE DAY")
            subTitle = find_shape_by_text(slide.shapes, "{DYNAMIC_FIELD FOR THOUGHT/JOKE/QUOTE}")
            if title:
                title.text = result['title']
            else:
                slide.shapes.title.text=result['title']
            if subTitle:
                subTitle.text = result['joke']
            elif slide.placeholders[1]:
                slide.placeholders[1].text=result['joke']
            unique_file_path = MEDIA_ROOT/ "ppt_modified" /f"{unique_filename}"
            root.save(unique_file_path)
            new_ppt.ppt_modified = str(unique_file_path)
            new_ppt.status = "finished"
            new_ppt.save()
        else:
            raise Exception("Result is empty")
        return {"id": new_ppt.id, "status": new_ppt.status, "created_at": new_ppt.created_at.isoformat()}
    except Exception as e:
        new_ppt.status = "failed"
        new_ppt.save()
        raise Exception(f"Error: {e}") from None

