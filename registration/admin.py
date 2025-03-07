from django.contrib import admin
from .models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('player_number', 'name', 'email', 'department', 'college', 'phone')
    ordering = ('player_number',)

admin.site.register(Registration, RegistrationAdmin)


# Register your models here.
