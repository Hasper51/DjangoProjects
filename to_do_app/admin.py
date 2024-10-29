from django.contrib import admin
from to_do_app.models import Todo
# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'user', 'status']
    readonly_fields = ['date', 'user']

