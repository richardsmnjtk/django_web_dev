from django.shortcuts import render

def index(request):
	return render(request,'index.html')
def crud(request):
	return render(request,'crud.html')

