from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#MainCategory 
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ImageField(upload_to='assets/category/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

#Sub Category 
class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.TextField()
    images = models.ImageField(upload_to='assets/subcategory/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name



#product With Description 
class Products(models.Model):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    description = models.TextField()
    images = models.ImageField(upload_to='assets/product/', blank=True, null=True)
    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length = 255)
    staff = models.CharField(max_length=255, blank = True)
    webiste = models.CharField(max_length=255, blank = True)
    schooltype = models.CharField(max_length=255, blank = True)
    org_size = models.CharField(max_length=255, blank = True)
    location = models.CharField(max_length=255, blank = True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

#Sclorship
class Sclorship(models.Model):
    name = models.CharField(max_length = 255)
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    description = models.TextField()
    images = models.ImageField(upload_to='assets/sclorship/', blank=True, null=True)

    def __str__(self):
        return self.name

#BrotherSisterCompany
class BrotherSisterCompany(models.Model):
    name = models.CharField(max_length = 255)
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    description = models.TextField()
    images = models.ImageField(upload_to='assets/brothersistercompany/', blank=True, null=True)
    
    def __str__(self):
        return self.name

