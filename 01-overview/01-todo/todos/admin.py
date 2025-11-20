from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "completed", "due_date", "created_at")
    list_filter = ("completed",)
    search_fields = ("title", "description")
    readonly_fields = ("created_at", "completed_at")
    ordering = ("-created_at",)
