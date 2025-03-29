from django.contrib import admin
from .models import Role
# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'created_date', 'modified_date']

admin.site.register(Role, RoleAdmin)

