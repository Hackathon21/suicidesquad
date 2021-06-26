from django.contrib import admin

from .models import *


admin.site.register(Doctor)
admin.site.register(Paitent)
admin.site.register(Appointment)

admin.site.register(Diagnosis)
admin.site.register(DiagnoseSlip)
admin.site.register(DiagnoseBill)


admin.site.register(Meds)
admin.site.register(MedsSlip)
admin.site.register(MedsBill)