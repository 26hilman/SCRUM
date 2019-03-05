from django import forms
from .models import Peminjaman
from django.db import models

class PostForm(forms.ModelForm):

   class Meta:
        model = Peminjaman
        fields = ('nama_barang', 'no_seri','kondisi_barang','id_karyawan', 'tanggal_pinjam', 'tanggal_kembali', 'keperluan', 'status')
        nama_barang = models.CharField(max_length=255)
        no_seri = models.CharField(max_length=255)
        kondisi_barang = models.CharField(max_length=255)
        id_karyawan = models.CharField(max_length=255)
        tanggal_pinjam = models.DateTimeField(("tanggal_pinjam"), auto_now=False, auto_now_add=False)
        tanggal_kembali = models.DateTimeField(("tanggal_kembali"), auto_now=False, auto_now_add=False)
        keperluan = models.CharField(max_length=255)
        status = models.CharField(max_length=255)
