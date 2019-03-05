from django.contrib import admin
from .models import *

# Register your models here.
model_barang = [Barang]
admin.site.register(model_barang)

model_peminjaman = [Peminjaman]
admin.site.register(model_peminjaman)