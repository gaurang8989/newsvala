from django.shortcuts import render,redirect
from.models import Khedut,Janvajevu,Lekh,Rajkaran,Dharmik,Swasthya,Samachar,About
# Create your views here.
def index(request):
    return redirect('/')

def khedut(request):

    kheduts = Khedut.objects.all()

    return render(request,'khedut.html',{'kheduts':kheduts})

def janvajevu(request):

    alljanvajevu = Janvajevu.objects.all()

    return render(request,'janvajevu.html',{'alljanvajevu':alljanvajevu})

def lekh(request):

    alllekh = Lekh.objects.all()
    return render(request,'lekh.html',{'alllekh':alllekh})

def rajkaran(request):

    allrajkaran = Rajkaran.objects.all()
    return render(request,'rajkaran.html',{'allrajkaran': allrajkaran})

def dharmik(request):

    alldharmik = Dharmik.objects.all()

    return render(request,'dharmik.html',{'alldharmik':alldharmik})

def swasthya(request):

    allswasthya = Swasthya.objects.all()

    return render(request,'swasthya.html',{'allswasthya':allswasthya})

def samachar(request):

    allsamachar = Samachar.objects.all()
    return render(request,'samachar.html',{'allsamachar':allsamachar})

def about(request):

    abouts = About.objects.all()

    return render(request,'about-us.html',{'abouts':abouts})