from django.contrib.gis.db import models


class OdpovednaOsoba(models.Model):
    jmeno = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Odpovědná osoba"
        verbose_name_plural = "Odpovědné osoby"

    def __str__(self):
        return self.jmeno


class Vlastnik(models.Model):
    jmeno = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Vlastník"
        verbose_name_plural = "Vlastníci"

    def __str__(self):
        return self.jmeno


class Rybnik(models.Model):
    nazev = models.CharField(max_length=255, verbose_name="Název")
    obec = models.CharField(max_length=255, verbose_name="Obec")
    okres = models.CharField(max_length=255, verbose_name="Okres")
    vodni_plocha = models.FloatField(verbose_name="Vodní plocha (ha)")
    vlastnik = models.ForeignKey(Vlastnik, on_delete=models.CASCADE, null=True, blank=True)
    odpovedna_osoba = models.ForeignKey(OdpovednaOsoba, on_delete=models.CASCADE, null=True, blank=True)
    polygon = models.PolygonField(verbose_name="Polygon", srid=4326)


    class Meta:
        verbose_name = "Rybník"
        verbose_name_plural = "Rybníky"

    def __str__(self):
        return self.nazev

class TBD(models.Model):
    rybnik = models.ForeignKey(Rybnik, on_delete=models.CASCADE)
    mimoradna_obchuzka = models.BooleanField(verbose_name="Mimorádná obchůzka", default=False)
    oblacnost = models.CharField(max_length=255, verbose_name="Oblačnost")
    vitr = models.CharField(max_length=255, verbose_name="Vítr", default="bezvětří")
    teplota = models.FloatField(verbose_name="Teplota °C")
    srazky = models.FloatField(verbose_name="Srážky (mm)", default=0)
    normalni_stav_hladiny = models.BooleanField(verbose_name="Normální stav hladiny", default=True)
    rozdil_stavu_hladiny = models.IntegerField(verbose_name="Rozdíl stavu hladiny (cm)", default=0)
    zavady = models.BooleanField(verbose_name="Závady", max_length=255, default=False)
    navrh_uprav = models.TextField(verbose_name="Návrh úprav v případě závad", null=True, blank=True)
    poznamka = models.CharField(verbose_name="Poznámka", max_length=255, null=True, blank=True)
    podpis = models.ImageField(verbose_name="Podpis", upload_to="podpisy", null=True, blank=True)

    class Meta:
        verbose_name = "TBD"
        verbose_name_plural = "TBD"