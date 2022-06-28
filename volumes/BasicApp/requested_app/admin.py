from django.contrib import admin

from .models import SimpleThing


class SimpleUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(SimpleThing, SimpleUserAdmin)
