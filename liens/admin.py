from django.contrib import admin
from .models import Client, Lien


class LienInline(admin.TabularInline):
    model = Lien
    extra = 1
    ordering = ['ordre']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['nom', 'code_unique', 'actif', 'liens_count', 'date_creation']
    list_filter = ['actif', 'date_creation']
    search_fields = ['nom', 'code_unique']
    readonly_fields = ['code_unique', 'date_creation']
    inlines = [LienInline]

    def liens_count(self, obj):
        return obj.liens_count

    liens_count.short_description = 'Nombre de liens'


@admin.register(Lien)
class LienAdmin(admin.ModelAdmin):
    list_display = ['titre', 'client', 'url', 'ordre', 'date_creation']
    list_filter = ['client', 'date_creation']
    search_fields = ['titre', 'client__nom']
    ordering = ['client', 'ordre']