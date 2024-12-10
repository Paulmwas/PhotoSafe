from django.db import models

# Create your models here.
class PhotoUploads(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo uploaded at {self.uploaded_at}"