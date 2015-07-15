from django.contrib import admin
from main.models import Morir, MorirCause

# Register your models here.
# class MorirInline(admin.TabularInline):
#     model = Morir


class MorirCauseAdmin(admin.ModelAdmin):
    ordering = ["cause"]
    list_display = ["cause"]
    search_fields = ["cause"]


class MorirCauseInline(admin.TabularInline):
    model = MorirCause
    readonly_fields = ["cause"]


class MorirAdmin(admin.ModelAdmin):
    ordering = ["number_of_deaths"]
    list_display = ["number_of_deaths", "sex", "year"]
    search_fields = ("sex", "year")
    inlines = [MorirCauseInline]


admin.site.register(Morir, MorirAdmin)
admin.site.register(MorirCause, MorirCauseAdmin)