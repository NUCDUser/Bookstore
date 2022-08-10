from distutils.sysconfig import customize_compiler
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CUSTOM_USER = get_user_model()


@admin.register(CUSTOM_USER)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CUSTOM_USER
    list_display = ['email', 'username', 'is_superuser']