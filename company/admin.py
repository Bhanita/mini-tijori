from django.contrib import admin
from .models import Company, Person

class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = ['name', 'amount', 'company']
    list_filter = ['name']
    search_field = ['name','company']

class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ['name','location','revenue']
    search_field = ['name','location']


admin.site.register(Company,CompanyAdmin)
admin.site.register(Person, PersonAdmin)

