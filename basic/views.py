from django.shortcuts import render , redirect
from .CITY_LIST import CITY_LIST
from .models import *
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponse

def home(request):
    return render(request , 'paitent/home.html')

def getDoctorCity(request):
    cities = []
    Doc = None
    for key,value in CITY_LIST:
        cities.append([key,value])
    if request.method == 'POST':
        city = request.POST.get('select')
        print(city)
        Doc = Doctor.objects.filter(city=city)
    context = {
        'cities': cities,
        'Doc': Doc
    }
    return render(request , 'paitent/getDoctorCity.html' , context)

def getDoctorCategory(request):
    category = Category.objects.all()
    params = {
        'category': category
    }
    return render(request , 'paitent/getDoctorCategory.html' , params)

def allDoctor(request, pk):
    doctor = Doctor.objects.filter(category__id=pk)
    category = Category.objects.get(id=pk)
    params = {
        'doctor': doctor,
        'category': category
    }
    return render(request , 'paitent/allDoctor.html', params)

def loginPage(request):
    if request.method == 'POST':
        uname  = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        user = authenticate(request , username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('<h2>Kon Bai? </h2>')

    return render(request , 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def newAppointment(request , pk):
    doctor = Doctor.objects.get(id=pk)
    paitent = Paitent.objects.get(user__username=request.user)
    if request.method == 'POST':
        date = request.POST.get('dateselect')
        appointment = Appointment.objects.create(doc = doctor , pai=paitent , status ='inactive' , due=date )
        appointment.save()
        messages.success(request , 'Appointment created')
    
    return redirect('home')