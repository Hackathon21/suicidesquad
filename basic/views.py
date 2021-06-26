from django.shortcuts import render, redirect
from .models import MedsSlip,MedsBill, Paitent , Appointment, Doctor, Meds, Diagnosis

def index(request):
    totalDoc = Doctor.objects.all().count()
    totalPai = Paitent.objects.all().count()
    meds = Meds.objects.all().count()
    params = {'total1': totalDoc, 'total2': totalPai , 'total3': meds}
    return render(request , 'index.html' , params )

def appointments(request):
    appointment = Appointment.objects.filter()
    context = {
        'appointment': appointment
    }
    return render(request, 'appointments/appointment.html' , context)
def newAppointment(request):
    docs = Doctor.objects.all()
    appointment = Appointment.objects.filter()
    print(appointment)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        doc1 = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        paitent = Paitent.objects.create(phone=phone , name=name)
        paitent.save()
        doctor = Doctor.objects.get(user__username=  doc1)
        print(doctor)
        appointment = Appointment.objects.create(doc=doctor , pai=paitent , date = date , time=time)
        appointment.save()
        return redirect('index')
    context = {
        'docs':docs,
        'appointment':appointment
    }
    return render(request , 'appointments/newAppointment.html' , context)

def inventory(request):
    meds = Meds.objects.filter()
    context = {
        'meds':meds
    }
    return render(request , 'inventory/inventory.html' ,context)

def inventoryUser(request):
    
    if request.method == 'POST' :
        phone = request.POST.get('phone')
        user, created = Paitent.objects.get_or_create(phone=phone)
        user.name = request.POST.get('name')
        user.save()
        return redirect('inventoryBill' ,user.id)
    context = {

    }
    return render(request , 'inventory/inventoryUser.html')

def inventoryBill(request, pk):
    user = Paitent.objects.get(id=pk)
    meds = Meds.objects.all()
    context ={
        'meds': meds,
        'user': user
    }
    return render(request, 'inventory/inventoryBill.html', context)


def inventoryBill2(request, pk , ls):
    profile = Paitent.objects.get(id=pk)
    item = Meds.objects.get(id=ls)
    orderItem,created = MedsSlip.objects.get_or_create(user=profile , ordered=False , item__id=item.id)
    order_qs = MedsBill.objects.filter(user=profile, active=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.meds.filter(item__id = med.id).exists():
            orderItem.qty = orderItem.qty + 1
            orderItem.save()
            messages.success(request , 'Qty updated')
            return redirect('index')
        else:
            meds.items.add(orderItem)
            messages.warning(request , 'new item')
            return redirect('appointments')
    else:
        
        order = MedsBill.objects.create(user=profile , ordered=False )
        order.meds.add(orderItem)
        messages.error(request , 'new order')
        return redirect('diagnoistss')
    


def allItems(request):
    meds = Meds.objects.filter()
    context = {
        'meds':meds
    }
    return render(request , 'inventory/allItems.html', context)

def newItem(request):
    items = Meds.objects.filter()
    if request.method == 'POST':
        name = request.POST.get('name')
        b_price = request.POST.get('b_price')
        s_price = request.POST.get('s_price')
        qty = request.POST.get('qty')
        item = Meds.objects.create(item=name, b_price=b_price , s_price=s_price, qty=qty)
        item.save()
        return redirect('newItem')
    context = {
        'items': items
    }
    return render(request , 'inventory/newItem.html', context)


def diagnoists(request):
    diagnosis = Diagnosis.objects.filter()
    context = {
        'diagnoists': diagnosis
    }
    return render(request , 'diagnoists/diagnoists.html' , context)

def allDiagnosis(request):
    pass

def newDiagnosis(request):
    diagnosis = Diagnosis.objects.filter()
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        diag = Diagnosis.objects.create(name=name, price=price)
        diag.save()
        return redirect('newDiagnosis')

    context = {
        'diagnosis': diagnosis
    }
    return render(request , 'diagnoists/newDiagnosis.html' ,context)

def diagnoistsBill(request):
    pass
from django.contrib.auth import login , logout , authenticate
def loginPage(request):
    if request.method == 'POST':
        uname  = request.POST.get('name')
        pwd = request.POST.get('pwd')
        user = authenticate(request , username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Please Login')
    return render(request , 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')