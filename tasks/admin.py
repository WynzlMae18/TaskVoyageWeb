from django.contrib import admin
from .models import CustomUser, EmailConfirmationToken

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'verified']
    # Add any other configurations you want for the admin panel

class EmailConfirmationTokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
    # Add any other configurations you want for the admin panel

# Register your models with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(EmailConfirmationToken, EmailConfirmationTokenAdmin)
