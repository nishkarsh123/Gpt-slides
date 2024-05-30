from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import send_generation_request_to_GPT_task
from django.shortcuts import render,redirect
from django.conf import settings
from .forms import PptxUploadForm
from django.urls import reverse
from .models import PPT
import uuid  # Import UUID module
from django.http import JsonResponse, FileResponse
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
import logging

MEDIA_ROOT=settings.MEDIA_ROOT

class uploadPPT(APIView):
    def post (self,request):
        form = PptxUploadForm(request.POST, request.FILES)
        if(request.method == "POST" and form.is_valid()):
            unique_filename = f"{uuid.uuid4()}.pptx"
            unique_file_path = MEDIA_ROOT/ "ppt" /f"{unique_filename}"
            new_ppt = PPT.objects.create(status="loading", ppt = str(unique_file_path),ppt_name = unique_filename)
            with open(unique_file_path, "wb") as file:
                for chunk in request.FILES["ppt"].chunks():
                    file.write(chunk)
            task = send_generation_request_to_GPT_task.delay(unique_filename,new_ppt.id)
            return redirect('/')
        context = {'form':form,"error":form.errors}
        return render(request, 'slides/slides.html', context)

def slides (request):
    form = PptxUploadForm()
    context = {'form':form}
    return render(request, 'slides/slides.html', context)


def ListPPT (request):
    ppt_list = PPT.objects.all()
    data = list(ppt_list.values('id', 'status', 'created_at', 'ppt_modified','ppt_name'))
    return JsonResponse(data,safe=False)


# @receiver(post_save, sender=PPT) 
# def save_profile(sender, instance, **kwargs):
#     unique_filename = f"{uuid.uuid4()}.pptx"
#     unique_file_path = MEDIA_ROOT/ "ppt" /f"{unique_filename}"
#     send_generation_request_to_GPT_task.delay(unique_filename,instance.id)