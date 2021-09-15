from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdmin(UserAdmin):
    list_display = ("email", "username", "date_joined", "is_admin")
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("user_image_origin", "email", "username", "password")}),
        ("info(各種情報)", {"fields": ("date_joined", "last_login")}),
        ("Permissions(権限管理)", {"fields": ("is_admin", "is_active")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide"),
            "fields": ("email", "username", "password1", "password2")
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
