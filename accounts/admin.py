from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts import models

User = get_user_model()


@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone', 'last_login',
                    'is_active', 'is_staff'
                    ]

    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Dates', {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'fields': (
                'email', 'first_name', 'last_name', 'phone',
                'password1', 'password2'
            )
        }),
    )
    search_fields = ['id', 'email', 'first_name', 'last_name', 'phone']
    ordering = ['email']
    filter_horizontal = ()
