from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model


User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (("User", {
        "fields": ("nome", "telefone", "cpf")
    }), ) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "nome", "is_superuser"]
    list_filter = []
    search_fields = ["username", "nome", ]