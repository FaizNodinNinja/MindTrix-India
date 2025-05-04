from django.contrib import admin
from .models import Service, ContactMessage
# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service', 'created_at')
    search_fields = ('name', 'email', 'phone', 'service__name')