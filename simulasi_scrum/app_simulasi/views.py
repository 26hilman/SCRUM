from django.shortcuts import render
from .form_peminjaman import PostForm

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