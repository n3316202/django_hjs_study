from django.contrib import admin

from todo.models import Profile, Todo
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Profile)

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
        "created_at",
        "updated_at"
    )

