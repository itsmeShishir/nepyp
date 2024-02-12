from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from auths.models import CustomUser
from  cloudinary.models import CloudinaryField

#Blog Category 
class CategoryBlog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

#Blog 
class Blog(models.Model):
    title = models.CharField(max_length=255)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category_name = models.ForeignKey(CategoryBlog, on_delete=models.CASCADE)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views_count = models.PositiveIntegerField(default=0)
    images = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title