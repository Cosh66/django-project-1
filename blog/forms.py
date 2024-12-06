from django import forms
from .models import Comment, UploadedImage

# Constants for validation
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
VALID_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/gif']


class UploadedImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a title for your image',
                'style': 'width: 100%; padding: 10px; font-size: 16px;',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'style': 'margin-top: 10px; font-size: 16px;',
            }),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')

        # Check for file size (limit: 5MB)
        if image and image.size > MAX_FILE_SIZE:
            raise forms.ValidationError("File size exceeds the 5MB limit. Please upload a smaller image.")

        # Check for allowed image types
        if image and image.content_type not in VALID_IMAGE_TYPES:
            raise forms.ValidationError("Invalid file format. Please upload an image in JPEG, PNG, or GIF format.")

        return image


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Write your comment here...',
                'rows': 3,
                'class': 'form-control',
            }),
        }

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if not body or len(body.strip()) < 5:
            raise forms.ValidationError("Comments must be at least 5 characters long.")
        return body