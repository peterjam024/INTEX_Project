from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Prescriber, Drugs, State

# Register your models here
admin.site.register(Prescriber)
admin.site.register(Drugs)
admin.site.register(State)
