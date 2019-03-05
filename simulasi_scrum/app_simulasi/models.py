from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

from django.db import models
from django.utils import timezone
# Create your models here.

class Karyawan(models.Model):
    nama = models.CharField(max_length=255)
    telepon = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Barang(models.Model):
    nama_barang = models.CharField(max_length=255)
    no_seri = models.CharField(max_length=255)
    kondisi_barang = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_barang

class Peminjaman(models.Model):
    nama_barang = models.CharField(max_length=255)
    no_seri = models.CharField(max_length=255)
    kondisi_barang = models.CharField(max_length=255)
    id_karyawan = models.CharField(max_length=255)
    tanggal_pinjam = models.CharField(max_length=255)
    tanggal_kembali = models.CharField(max_length=255)
    keperluan = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_barang
