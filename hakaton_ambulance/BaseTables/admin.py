from django.contrib import admin
from .models import Interval, Cabinet, Patient

# Register your models here.
@admin.register(Interval)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id_interval', 'time_start', 'time_end']


@admin.register(Cabinet)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id_cabinet', 'numder', 'special', 'doctor']


@admin.register(Patient)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id_patient', 'name', 'age', 'snils', 'polis']
