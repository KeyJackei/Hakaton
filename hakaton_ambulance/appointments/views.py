from django.shortcuts import render
from BaseTables.models import Cabinet

def appointment_form(request):
    specialists = Cabinet.objects.all()
    return render(request, 'appointments/form.html', {'specialists': specialists})
