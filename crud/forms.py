from django import forms
from crud.models import *

class Request(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ('nama_pelanggan','nim_pelanggan','jenis_kelamin','alamat')