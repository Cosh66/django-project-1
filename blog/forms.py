from django import forms
from .models import Comment, UploadedImage


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
        if image and image.size > 5 * 1024 * 1024:  # 5MB in bytes
            raise forms.ValidationError("The maximum file size allowed is 5MB.")

        # Check for allowed image types
        valid_image_types = ['image/jpeg', 'image/png', 'image/gif']
        if image and image.content_type not in valid_image_types:
            raise forms.ValidationError(
                "Only JPEG, PNG, and GIF image formats are supported."
            )

        return image


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']  # Ensure 'body' exists in the Comment model
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Write your comment here...',
                'rows': 3,
                'class': 'form-control',
            }),
        }