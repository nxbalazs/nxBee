from django.contrib import admin
from hive_management.models import Hive, Inspection, Treatment, Note

# Register your models here.
class HiveAdmin(admin.ModelAdmin):
    pass

class InspectionAdmin(admin.ModelAdmin):
    pass

class TreatmentAdmin(admin.ModelAdmin):
    pass

class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hive, HiveAdmin)
admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Note, NoteAdmin)