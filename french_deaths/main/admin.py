from django.contrib import admin
from main.models import Morir

# Register your models here.
# class MorirInline(admin.TabularInline):
#     model = Morir


class MorirAdmin(admin.ModelAdmin):
    list_display = ("cause_of_death", "sex", "number_of_deaths", "year")
    

admin.site.register(Morir, MorirAdmin)
