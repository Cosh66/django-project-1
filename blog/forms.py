from django import forms
from .models import UploadedImage  # Make sure this model is defined in models.py

class UploadedImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage  # Reference the UploadedImage model
        fields = ['title', 'image']  # Fields to include in the form