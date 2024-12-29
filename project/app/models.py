from django.db import models

class Siswa(models.Model):
    id = models.AutoField(primary_key=True)
    nis = models.IntegerField()
    nama = models.CharField(max_length=100)
    kelas = models.IntegerField()
    alamat = models.CharField(max_length=100)

    def __str__(self):
        return self.name