from django.db import models
from django.utils import timezone
# Create your models here.
class Karyawan(models.Model):
    nama = models.CharField(max_length=255)
    telepon = models.CharField(max_length=255)

    def __str__(self):
        return self.nama