from django.contrib import admin

from db.models import Company, Organization, Person, Politician, Sector

class BaseAdmin(admin.ModelAdmin):
    search_fields = ['name']


class CompanyAdmin(BaseAdmin):
    list_display = ('name', 'address', 'employees', 'address', 'url')


class OrganizationAdmin(BaseAdmin):
    list_display = ('name', 'activity', 'address', 'url')


class PersonAdmin(BaseAdmin):
    list_display = ('name', 'profession', 'country', 'url')


class PoliticianAdmin(BaseAdmin):
    list_display = ('name', 'function', 'country', 'url')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Politician, PoliticianAdmin)
admin.site.register(Sector)
