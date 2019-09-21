from django.shortcuts import render, get_object_or_404, redirect
# from webapp.forms import ProductForm
from webapp.models import Register


def index_view(request, *args, **kwargs):
    registers = Register.objects.filter(status='active').order_by('-create')
    return render(request, 'index.html', context={
        'registers': registers
    })


