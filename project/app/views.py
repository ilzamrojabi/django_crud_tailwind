from django.shortcuts import render, redirect
from .forms import siswaForm
from .models import Siswa


def home(request):
    return render(request, 'app/index.html')

def siswa_create(request):
    form = siswaForm()
    if request.method == 'POST':
        form = siswaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('siswa_read')
    return render(request, 'app/tambah.html', {'form':form})

def siswa_read(request):
    siswa = Siswa.objects.all()
    return render(request, 'app/index.html', {'siswa':siswa})

def siswa_update(request, id):
    siswa = Siswa.objects.get(id=id)
    form = siswaForm(instance=siswa)
    if request.method == 'POST':
        form = siswaForm(request.POST, instance=siswa)
        if form.is_valid():
            form.save()
        return redirect('siswa_read')
    return render(request, 'app/tambah.html', {'form':form})

def siswa_delete(request, id):
    siswa = Siswa.objects.get(id=id)
    if request.method == 'POST':
        siswa.delete()
        return redirect('siswa_read')
    return render(request, 'app/delete.html', {'siswa':siswa})