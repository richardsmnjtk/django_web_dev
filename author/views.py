from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'author.html')

def Richard(request):
	context = {
		'nama':'Richard Bina Jadi Simanjuntak',
		'profesi':'Nim : 1101184245 | Mahasiswa | Teknik Telekomunikasi ',
		'nim':'1101184245',
		'no':'1',
		'foto1':'/static/img/pfr.jpg',
		'foto2':'/static/img/1.png',
		'foto3':'/static/img/2.png',
		'foto4':'/static/img/3.png',
		'foto5':'/static/img/4.png',
		'foto6':'/static/img/5.png',
		'foto7':'/static/img/6.png',
		'deskripsi0':'Nama lengkap saya Richard Bina Jadi Simanjuntak dan saya sekarang berumur 20 tahun. Saya mampu berkomunikasi dengan Bahasa Indonesia dan Bahasa Inggris.',
		'deskripsi1':'Saya adalah seorang mahasiswa Teknik Telekomunikasi, dan berkuliah di Telkom University. Saya sangat menyukai teknologi terbaru yang baru diluncurkan. Saya senang mengeksplorasi hal hal yang menyangkut IT.',
	}
	return render(request,'isiauthor.html',context)

def Christian(request):
	context = {
		'nama':'Christian Pratama Sitepu',
		'profesi':'Nim : 1101183438 | Mahasiswa | Teknik Telekomunikasi ',
		'nim':'1101183438',
		'no':'1',
		'foto1':'/static/img/pfc.jpg',
		'foto2':'/static/img/1.png',
		'foto3':'/static/img/2.png',
		'foto4':'/static/img/3.png',
		'foto5':'/static/img/4.png',
		'foto6':'/static/img/5.png',
		'foto7':'/static/img/6.png',
		'deskripsi0':'Nama lengkap saya Christian Pratama Sitepu dan saya sekarang berumur 20 tahun. Saya mampu berkomunikasi dengan Bahasa Indonesia dan Bahasa Inggris.',
		'deskripsi1':'Saya adalah seorang mahasiswa Teknik Telekomunikasi, dan berkuliah di Telkom University. Saya sangat menyukai teknologi terbaru yang baru diluncurkan. Saya senang mengeksplorasi hal hal yang menyangkut IT.',
	}
	return render(request,'isiauthor.html',context)



def Pelanggan(request):
	context={
		'nama':'Portal Pelanggan'
	}
	return render(request,'mhs.html',context)

def Crew(request):
	context={
		'nama':'Portal Crew'
	}
	return render(request,'Dosen.html',context)
