from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    data = demotable.objects.all()
    context = {'data':data}
    return render(request, 'index.html',context)