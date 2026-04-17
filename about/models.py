from django.db import models
from django_summernote.fields import SummernoteTextField
from cloudinary.models import CloudinaryField

class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1500)

    def __str__(self):
        return self.title
    
class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"

