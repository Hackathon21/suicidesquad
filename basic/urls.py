from django.urls import path,  include
from . import views
urlpatterns = [
    path('' , views.index , name='index'),

    #Appointments
    path('appointments' , views.appointments , name='appointments'),
    path('newAppointment' , views.newAppointment , name='newAppointment'),

    #inventory
    path('inventory' , views.inventory , name='inventory'),
    path('allItems' , views.allItems , name='allItems'),
    path('newItem' , views.newItem , name='newItem'),
    path('inventoryUser' , views.inventoryUser , name='inventoryUser'),

    
    path(r'^inventoryBill/(?P<pk>\w+)/$' , views.inventoryBill , name='inventoryBill'),
    path(r'^inventoryBill/(?P<pk>\w+)/(?P<ls>\w+)/$' , views.inventoryBill2 , name='inventoryBill2'),

    #diagnoists
    path('diagnoists' , views.diagnoists , name='diagnoists'),
    path('newDiagnosis', views.newDiagnosis , name='newDiagnosis'),

    #auth
    path('loginPage' , views.loginPage , name='loginPage'),
    path('logoutPage' , views.logoutPage , name='logoutPage')
]