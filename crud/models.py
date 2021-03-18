
from __future__ import unicode_literals
from django.db import models

# Create your models here.

    
class Mahasiswa(models.Model):
    SEX_CHOICES = (
        ('Perempuan', 'Perempuan',),
        ('Laki-laki', 'Laki-laki',),
        
    )
    nama_mahasiswa = models.CharField(max_length=100)
    nim_mahasiswa = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(
        max_length=15,
        choices=SEX_CHOICES,
    )
    alamat = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_mahasiswa

