from pickletools import read_unicodestring1
from django.shortcuts import render
from primeraApp.models import empleados

def empleadosData(request):
    e = empleados.objects.all()
    data = {'empleados': e}
    return render(request,'primeraApp/index.html', data)


# Create your views here.
