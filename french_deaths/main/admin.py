from django.contrib import admin
from main.models import Morir

# Register your models here.
# class MorirInline(admin.TabularInline):
#     model = Morir

class MorirAdmin(admin.ModelAdmin):
    list_display = ("cause_of_death", "year", "country", "sex", "number_of_deaths")
    search_fields = ["year", "sex", "cause of death"]
    # inlines = [MorirInline]

admin.site.register(Morir, MorirAdmin)