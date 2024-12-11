from django.contrib import admin
from .models import Student, Staff, DisciplinaryIncident, Sanction, SeverityLevel

admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(DisciplinaryIncident)
admin.site.register(Sanction)
admin.site.register(SeverityLevel)
