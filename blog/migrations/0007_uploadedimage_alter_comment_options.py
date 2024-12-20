# Generated by Django 4.2.16 on 2024-11-28 21:53

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uploaded_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
    ]
