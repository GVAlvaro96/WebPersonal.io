from django.contrib import admin
from .models import Project

# Register your models here.
class PojectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')



admin.site.register(Project, PojectAdmin)