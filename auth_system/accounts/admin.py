from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'name',
        'is_staff',
    ]

    fieldsets = (
    (None, {"fields": ("email", "password")}),
    ("Personal info", {"fields": ("name", "username")}),
    ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    ("Important dates", {"fields": ("last_login", "date_joined")}),)
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'password1', 'password2'),
        }),
    )

    ordering = ('email',)

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)

