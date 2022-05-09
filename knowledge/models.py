from django.urls import reverse_lazy
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import CustomUser

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField('Manufacturer name:',max_length = 128, unique=True)
    created_date = models.DateField(auto_now = True)
    updated_date  = models.DateField(auto_now_add = True)
    created_by = models.ForeignKey(CustomUser, null = True, on_delete = models.SET_NULL)

  
    def get_delete_url(self):
        return reverse_lazy('manufacturer-delete', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('manufacturer-update', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=128)
    created_date = models.DateField(auto_now=True)
    updated_date  = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Equipment(models.Model):
    name  = models.CharField(max_length=128)
    manufacturer = models.ForeignKey(Manufacturer, null = True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    image = models.ImageField(upload_to='equipment', default='media/equipment/no_image_available.png')

    def __str__(self):
        return f'{self.name}'


class Error(models.Model):
    code = models.CharField(max_length=256)
    message = models.CharField(max_length=256)
    issues = models.CharField(max_length=256)
    created_date = models.DateField(auto_now = True)
    updated_date  = models.DateField(auto_now_add = True)
    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE)
    solution = RichTextUploadingField()
    created_by = models.ForeignKey(CustomUser, null = True, on_delete = models.SET_NULL)
