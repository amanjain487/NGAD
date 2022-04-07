from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'wasMarksUser'
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Additional info', {
            'fields': ('wasMarksUser',)
        }),
        ('Permissions', {
            'fields': (
                'is_superuser',
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Additional info', {
            'fields': ('wasMarksUser',)
        }),
        ('Permissions', {
            'fields': (
                'is_superuser',
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register([File, Category, DownloadLogs])

