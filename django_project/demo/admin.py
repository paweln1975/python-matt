from django.contrib import admin
from .models import Role, Person
# Register your models here.

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'created_date', 'modified_date']

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'created_date', 'modified_date']


