from django.urls import path
from . import views

urlpatterns = [
    path ('peminjaman/', views.tampilan_peminjaman, name='form_pinjam')
]