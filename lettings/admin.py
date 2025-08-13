from django.contrib import admin
from lettings.models import Address, Letting


class AdressAdmin(admin.ModelAdmin):
    list_display = ('number', 'street', 'city', 'state',
                    'zip_code', 'country_iso_code')
    list_filter = ['state']


class LettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'address')


admin.site.register(Address, AdressAdmin)
admin.site.register(Letting, LettingAdmin)
