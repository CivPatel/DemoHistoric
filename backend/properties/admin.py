from django.contrib import admin
from .models import Property, Owner, Tenant

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("address","owner","built_year","is_public")
    list_filter = ("is_public","built_year")
    search_fields = ("address","owner__name")

admin.site.register(Owner)
admin.site.register(Tenant)