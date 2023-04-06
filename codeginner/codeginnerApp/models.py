from distutils.command.upload import upload
from sys import maxsize
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class contentRegister(models.Model):
    id=models.AutoField(primary_key=True)
    chTitle=models.CharField(max_length=255)
    chName=models.CharField(max_length=255)
    chTheory=RichTextField(max_length=3000)
    chVideo=models.FileField(upload_to='videos',blank=True)
    chExample=models.URLField(max_length=200)
    objects=models.Manager()

    def __str__(self):
        return self.chTitle