from django.contrib import admin

from todo.models import Todo, User

admin.site.register(User)

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
        "created_at",
        "updated_at"
    )

