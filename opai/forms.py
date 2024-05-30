from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.translation import gettext_lazy as _
from pptx import Presentation
from .models import PPT

class PptxUploadForm(forms.ModelForm):
    class Meta:
        model = PPT
        fields = ('ppt',)
        labels = {
            'ppt': '',
        }
        widgets = {
            'ppt': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }

    def clean_ppt(self):
        ppt = self.cleaned_data.get('ppt', False)
        
        if not ppt:
            raise ValidationError('No file was submitted.')
        
        if not ppt.name.endswith('.pptx'):
            raise ValidationError('File must be a .pptx file.')

        try:
            Presentation(ppt)
        except Exception as e:
            raise ValidationError('File is not a valid PPTX: {}'.format(str(e)))

        return ppt
