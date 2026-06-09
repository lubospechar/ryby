from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from rybniky.models import Rybnik, Vlastnik, OdpovednaOsoba, TBD


@admin.register(Vlastnik)
class VlastnikAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "telefon")

@admin.register(OdpovednaOsoba)
class OdpovednaOsobaAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "telefon")


@admin.register(Rybnik)
class RybnikAdmin(LeafletGeoAdmin):
    list_display = ("nazev", "vodni_plocha", "obec", "okres")
    list_filter = (
        "obec",
        "okres",
    )
    search_fields = ("nazev",)
    ordering = ("nazev",)
    leaflet_default_lon = 15
    leaflet_default_lat = 50
    leaflet_default_zoom = 7


@admin.register(TBD)
class TBDAdmin(admin.ModelAdmin):
    list_display = (
        "rybnik",
        "mimoradna_obchuzka",
        "teplota",
        "srazky",
        "normalni_stav_hladiny",
        "rozdil_stavu_hladiny",
    )
    list_filter = (
        "rybnik",
        "mimoradna_obchuzka",
        "normalni_stav_hladiny",
    )
    search_fields = (
        "rybnik__nazev",
        "oblacnost",
        "vitr",
        "zavady",
        "poznamka",
    )
    ordering = ("rybnik__nazev",)
    autocomplete_fields = ("rybnik",)

    fieldsets = (
        (
            "Základní údaje",
            {
                "fields": (
                    "rybnik",
                    "mimoradna_obchuzka",
                )
            },
        ),
        (
            "Počasí",
            {
                "fields": (
                    "oblacnost",
                    "vitr",
                    "teplota",
                    "srazky",
                )
            },
        ),
        (
            "Stav hladiny",
            {
                "fields": (
                    "normalni_stav_hladiny",
                    "rozdil_stavu_hladiny",
                )
            },
        ),
        (
            "Závady a návrh úprav",
            {
                "fields": (
                    "zavady",
                    "navrh_uprav",
                )
            },
        ),
        (
            "Poznámka a podpis",
            {
                "fields": (
                    "poznamka",
                    "podpis",
                )
            },
        ),
    )
