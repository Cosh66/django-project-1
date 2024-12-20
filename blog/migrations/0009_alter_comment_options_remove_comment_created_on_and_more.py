# Generated by Django 4.2.16 on 2024-12-04 12:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_delete_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.uploadedimage'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
