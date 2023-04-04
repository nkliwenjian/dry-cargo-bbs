from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from dry_cargo_bbs.apps.accounts.models import User


admin.site.register(User, UserAdmin)
