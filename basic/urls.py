from django.urls import path , include
from . import views

urlpatterns = [
    
    path('' ,views.home , name='home'),
    path('getDoctorCity' , views.getDoctorCity , name='getDoctorCity'),
    path('getDoctorCategory' , views.getDoctorCategory , name='getDoctorCategory'),
    path('allDoctor/<str:pk>/' , views.allDoctor , name='allDoctor'),


    #auth
    path('login' , views.loginPage , name='loginPage'),
    path('logout' , views.logoutPage , name='logoutPage'),

    #appointment
    path('newAppointment/<str:pk>/' , views.newAppointment , name='newAppointment'),
]