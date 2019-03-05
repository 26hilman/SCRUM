from django.shortcuts import render
from .form_peminjaman import PostForm
from .models import *

def home(request):
    return render(request, 'home/daftar_home.html',{})
# Create your views here.
def tampilan_peminjaman(request):
    return render(request, 'peminjaman.html', {})

def form_pinjam(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save
            form.save()
            return redirect('form_pinjam')
    else :
        form = PostForm()
    return render(request, 'peminjaman.html', {'form' : form})

def display_pinjam(request):
    pinjam_semua = Barang.objects.all()
    return render(request, 'DisplayPeminjaman.html', {'display_data': pinjam_semua})
