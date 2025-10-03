# clients/admin.py

from django.contrib import admin
from .models import Client  # Import the Client model

# Register your models here.
admin.site.register(Client)