from app.models import Portifolio, Projetos
from django.contrib import admin

# Register your models here.
@admin.register(Portifolio)
class PortifolioAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "image",
        "created",
        "modified",
        ]
    list_filter = ["name", "created", "modified"]
    list_editable = ["image"]

@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "image",
        "created",
        "modified",
        ]
    list_filter = ["name", "created", "modified"]
    list_editable = ["image"]