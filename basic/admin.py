from django.contrib import admin

from .models import *

admin.site.register(Doctor)
admin.site.register(Paitent)
admin.site.register(Category)
admin.site.register(Appointment)
