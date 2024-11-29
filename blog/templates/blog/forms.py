from django import forms
from .models import UploadedImage

class UploadedImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage  # Reference to the UploadedImage model
        fields = ['title', 'image']  # Fields to include in the form