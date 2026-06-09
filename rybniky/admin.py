from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from rybniky.models import Rybnik, Vlastnik, OdpovednaOsoba, TBD, Ryba


@admin.register(Vlastnik)
class VlastnikAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "telefon")

@admin.register(OdpovednaOsoba)
class OdpovednaOsobaAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "telefon")


@admin.register(Rybnik)
class RybnikAdmin(LeafletGeoAdmin):
    list_display = (
        "nazev",
        "okres",
        "kraj",
        "charakter",
        "katastralni_vodni_plocha",
        "zatopena_vodni_plocha",
    )
    list_filter = (
        "kraj",
        "okres",
        "charakter",
    )
    search_fields = (
        "nazev",
        "katastralni_obec",
        "parcely",
        "okres",
        "kraj",
    )
    ordering = ("nazev",)


    leaflet_default_lon = 15
    leaflet_default_lat = 50
    leaflet_default_zoom = 7

    fieldsets = (
        (
            "Základní údaje",
            {
                "fields": (
                    "nazev",
                    "charakter",
                    "pouziti",
                )
            },
        ),
        (
            "Umístění",
            {
                "fields": (
                    "kraj",
                    "okres",
                    "katastralni_obec",
                    "parcely",
                )
            },
        ),
        (
            "Parametry rybníka",
            {
                "fields": (
                    "katastralni_vodni_plocha",
                    "zatopena_vodni_plocha",
                    "hloubka",
                    "doba_nahaneni",
                    "doba_vypousteni",
                )
            },
        ),
        (
            "Osoby",
            {
                "fields": (
                    "vlastnik",
                    "odpovedna_osoba",
                )
            },
        ),
        (
            "Mapa",
            {
                "fields": (
                    "polygon",
                )
            },
        ),
    )


@admin.register(TBD)
class TBDAdmin(admin.ModelAdmin):
    list_display = (
        "rybnik",
        'datum',
        "mimoradna_obchuzka",
        "teplota",
        "srazky",
        "normalni_stav_hladiny",
        "rozdil_stavu_hladiny",
    )
    list_filter = (
        "rybnik",
        'datum',
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
                    'datum'
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


@admin.register(Ryba)
class RybaAdmin(admin.ModelAdmin):
    list_display = (
        "jmeno",
        "znacka",
    )