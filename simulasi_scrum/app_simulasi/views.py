from django.shortcuts import render

def home(request):
    return render(request, 'home/daftar_home.html',{})
# Create your views here.
def tampilan_peminjaman(request):
    return render(request, 'peminjaman.html', {})

def form_pinjam(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            #post = form.save
            form.save()
            # return redirect('')
    else :
        form = BlogForm()
    return render(request, 'peminjaman.html', {'form' : form})