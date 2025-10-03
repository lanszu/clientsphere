# clients/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Client
from .forms import ClientForm

# --- CRUD Views (already exist) ---
@login_required
def dashboard(request):
    query = request.GET.get('q')
    clients = Client.objects.all()
    if query:
        clients = clients.filter(name__icontains=query)
    context = {'clients': clients}
    return render(request, 'clients/dashboard.html', context)

@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ClientForm()
    return render(request, 'clients/add_client.html', {'form': form})

@login_required
def update_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/update_client.html', {'form': form, 'client': client})

@login_required
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('dashboard')
    return render(request, 'clients/delete_client.html', {'client': client})


# --- NEW AUTHENTICATION VIEWS ---

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'clients/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'clients/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')