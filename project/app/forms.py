from django import forms
from .models import Siswa

class siswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = '__all__'
        labels = {
            'id': 'ID',
            'nis': 'Nis',
            'nama': 'Nama',
            'kelas': 'Kelas',
            'Alamat': 'Alamat',
        }
        widgets = {
            'id': forms.NumberInput(attrs={'placeholder': 'id', 'class': 'form-control'}),
            'nis': forms.NumberInput(attrs={'placeholder': 'Masukkan Nomor Nis', 'class': 'forms-control'}),
            'nama': forms.TextInput(attrs={'placeholder': 'Masukkan Nama', 'class': 'forms-control'}),
            'kelas': forms.NumberInput(attrs={'placeholder': 'Masukkan Kelas Anda', 'class':'forms-control'}),
            'alamat': forms.TextInput(attrs={'placeholder': 'Masukkan Alamat Anda', 'class': 'forms-control'}),
        }