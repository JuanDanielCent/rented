from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Property, Property_lease
from .forms import PropertyForm, LeaseForm, CategoriaForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'])
                user.save()
                login(request, user)
                return redirect('index')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already created'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Passwords do not match'
        })
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })

def signin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Username or password incorrect'
            })
        else:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html', {
        'form': AuthenticationForm
    })

@login_required
def signout(request):
    logout(request)
    return redirect('index')

@login_required
def venta(request):
    propiedad = Property.objects.all()
    return render(request, 'venta/venta.html', {
        'propiedad': propiedad, 'user': request.user
    })

@login_required
def alquiler(request):
    propiedad = Property_lease.objects.all()
    return render(request, 'alquiler/alquiler.html', {
        'propiedad': propiedad, 'user': request.user
    })

@login_required
def add_property(request):
    form = PropertyForm(request.POST or None)
    if form.is_valid():
        venta = form.save(commit=False)
        venta.user = request.user
        venta.save()
        return redirect('venta')
    return render(request, 'venta/add_property.html', {
        'form': PropertyForm
    })

@login_required
def add_lease(request):
    form = LeaseForm(request.POST or None)
    if form.is_valid():
        alquiler = form.save(commit=False)
        alquiler.user = request.user
        alquiler.save()
        return redirect('alquiler')
    return render(request, 'alquiler/add_lease.html', {
        'form': PropertyForm
    })

@login_required
def elegir_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.cleaned_data['categoria']
            if categoria == 'venta':
                return redirect('add_property')
            else:
                return redirect('add_lease')

    form = CategoriaForm()
    return render(request, 'elegir_categoria.html', {
        'form': form
    })

@login_required
def update_venta(request, pk):
    venta = get_object_or_404(Property, pk=pk)
    form = PropertyForm(request.POST or None, instance=venta)
    if form.is_valid():
        venta= form.save(commit=False)
        venta.user = request.user
        venta.save()
        return redirect('venta')
    return render(request, 'venta/update_venta.html', {
        'venta': venta,
        'form': form
    })

@login_required
def delete_venta(request, pk):
    venta = get_object_or_404(Property, pk=pk)
    venta.delete()
    return redirect('venta')

@login_required
def update_alquiler(request, pk):
    alquiler = get_object_or_404(Property_lease, pk=pk)
    form = LeaseForm(request.POST or None, instance=alquiler)
    if form.is_valid():
        alquiler = form.save(commit=False)
        alquiler.user = request.user
        alquiler.save()
        return redirect('alquiler')
    return render(request, 'alquiler/update_alquiler.html', {
        'alquiler': alquiler,
        'form': form
    })

@login_required
def delete_alquiler(request, pk):
    alquiler = get_object_or_404(Property_lease, pk=pk)
    alquiler.delete()
    return redirect('alquiler')