from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from import_export.admin import ExportMixin, ImportExportMixin

from .forms import UserChangeForm, UserCreationForm
from .models import User, Address


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0
    classes = ['collapse']


@admin.register(User)
class UserAdmin(ImportExportMixin, BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    fieldsets = (
        (_('General'), {
            'fields': (
                'email',
                'password',
                'first_name',
                'last_name',
                'last_login'
            )
        }),
        (_('Details'), {
            'fields': (
                'avatar',
                'biography',
                'date_of_birth',
                'sex',
                'telephone',
                'mobile',
                'share_code',
                'date_joined'
            )
        }),
        (_('Permissions'), {
            'classes': ('collapse',),
            'fields': (
                'is_staff',
                'is_superuser',
                'is_active',
            )
        }),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (_('General'), {
            'fields': (
                'email',
                'password1',
                'password2'
            )
        }),
        (_('Details'), {
            'fields': (
                'avatar',
                'biography',
                'date_of_birth',
                'sex',
                'share_code',
                'telephone',
                'mobile'
            )
        }),
        (_('Permissions'), {
            'classes': ('collapse',),
            'fields': (
                'is_staff',
                'is_superuser',
                'is_active'
            )
        }),
    )
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    readonly_fields = (
        'date_joined',
        'share_code',
        'last_login',
        'updated_at',
    )
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active'
    )
    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
        'groups'
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
    )
    ordering = ('-id',)
    filter_horizontal = ()

    save_on_top = True
    list_per_page = 30
    inlines = [
        AddressInline,
    ]

    def has_delete_permission(self, request, obj=None):
        return False
