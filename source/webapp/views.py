from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import RegisterForm
from webapp.models import Register


def index_view(request, *args, **kwargs):
    registers = Register.objects.filter(status='active').order_by('-create')
    return render(request, 'index.html', context={
        'registers': registers
    })

def register_add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register_add.html', context={'form': form})
    elif request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            register = Register.objects.create(
                author=data['author'],
                email=data['email'],
                text=data['text'],
            )
            return redirect('index')
        else:
            return render(request, 'register_add.html', context={'form': form})
