from django.contrib.gis.db import models


class OdpovednaOsoba(models.Model):
    jmeno = models.CharField(max_length=255, unique=True)
    telefon = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Odpovědná osoba"
        verbose_name_plural = "Odpovědné osoby"

    def __str__(self):
        return self.jmeno


class Vlastnik(models.Model):
    jmeno = models.CharField(max_length=255, unique=True)
    telefon = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Vlastník"
        verbose_name_plural = "Vlastníci"

    def __str__(self):
        return self.jmeno


class Rybnik(models.Model):
    class CharakterRybnika(models.TextChoices):
        SILNE = "silne", "Silně průtočný"
        SLABE = "slabe", "Slabě průtočný"
        NEBEZKY = "nebezky", "Nebezký"

    class Pouziti(models.TextChoices):
        VYTAZNIK = "vytaznik", "Výtažník"
        KOMORA = "komora", "Komora"
        HLAVNI = "hlavni", "Hlavní rybník"

    nazev = models.CharField(max_length=255, verbose_name="Název", unique=True)
    katastralni_obec = models.CharField(max_length=255, verbose_name="Katastrální obec")
    parcely = models.CharField(
        max_length=255, verbose_name="Parcely", null=True, blank=True
    )
    okres = models.CharField(max_length=255, verbose_name="Okres")
    kraj = models.CharField(max_length=255, verbose_name="Kraj")
    katastralni_vodni_plocha = models.FloatField(
        verbose_name="Katastrální vodní plocha (ha)"
    )
    zatopena_vodni_plocha = models.FloatField(verbose_name="Zatopená vodní plocha (ha)")
    hloubka = models.FloatField(verbose_name="Hloubka (m)")
    charakter = models.CharField(
        max_length=255,
        choices=CharakterRybnika.choices,
        verbose_name="Charakter rybníka",
    )
    pouziti = models.CharField(
        max_length=255, choices=Pouziti.choices, verbose_name="Použití"
    )
    doba_nahaneni = models.IntegerField(verbose_name="Doba náhánění (dny)")
    doba_vypousteni = models.IntegerField(verbose_name="Doba výpouštění (dny)")

    vlastnik = models.ForeignKey(
        Vlastnik, on_delete=models.CASCADE, null=True, blank=True
    )
    odpovedna_osoba = models.ForeignKey(
        OdpovednaOsoba, on_delete=models.CASCADE, null=True, blank=True
    )
    polygon = models.PolygonField(verbose_name="Polygon", srid=4326)

    class Meta:
        verbose_name = "Rybník"
        verbose_name_plural = "Rybníky"

    def __str__(self):
        return self.nazev


class Ryba(models.Model):
    jmeno = models.CharField(max_length=255)
    znacka = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.jmeno} ({self.znacka})"

    class Meta:
        verbose_name = "Ryba"
        verbose_name_plural = "Ryby"


class Produkce(models.Model):
    class NasazenoVyloveno(models.TextChoices):
        NASAZENO = "nasazeno", "Nasazeno"
        VYLOVENO = "vyloveno", "Vyloveno"

    rybnik = models.ForeignKey(Rybnik, on_delete=models.CASCADE)
    datum = models.DateField(verbose_name="Datum")
    nasazeno_vyloveno = models.CharField(
        max_length=255,
        choices=NasazenoVyloveno.choices,
        verbose_name="Nasazeno/vyloveno",
    )
    ryba = models.ForeignKey(Ryba, on_delete=models.CASCADE)
    puvod = models.CharField(
        max_length=255, verbose_name="Původ", null=True, blank=True
    )
    zdroj = models.ForeignKey(
        Rybnik,
        on_delete=models.CASCADE,
        verbose_name="Zdroj",
        null=True,
        blank=True,
        related_name="zdroj_produktu",
    )
    stari = models.PositiveIntegerField(verbose_name="Stáří (roky)")
    rychlenka = models.BooleanField(verbose_name="Rychlenka", default=False)
    ks = models.PositiveIntegerField(verbose_name="Ks", null=True, blank=True)
    hmotnost = models.IntegerField(verbose_name="Hmotnost (kg)", null=True, blank=True)
    cena_kg = models.IntegerField(verbose_name="Cena za kg", null=True, blank=True)

    class Meta:
        verbose_name = "Produkce"
        verbose_name_plural = "Produkce"


class TBD(models.Model):
    rybnik = models.ForeignKey(Rybnik, on_delete=models.CASCADE)
    datum = models.DateTimeField(verbose_name="Datum a čas")
    mimoradna_obchuzka = models.BooleanField(
        verbose_name="Mimorádná obchůzka", default=False
    )
    oblacnost = models.CharField(max_length=255, verbose_name="Oblačnost")
    vitr = models.CharField(max_length=255, verbose_name="Vítr", default="bezvětří")
    teplota = models.FloatField(verbose_name="Teplota °C")
    srazky = models.FloatField(verbose_name="Srážky (mm)", default=0)
    normalni_stav_hladiny = models.BooleanField(
        verbose_name="Normální stav hladiny", default=True
    )
    rozdil_stavu_hladiny = models.IntegerField(
        verbose_name="Rozdíl stavu hladiny (cm)", default=0
    )
    zavady = models.BooleanField(verbose_name="Závady", max_length=255, default=False)
    navrh_uprav = models.TextField(
        verbose_name="Návrh úprav v případě závad", null=True, blank=True
    )
    poznamka = models.CharField(
        verbose_name="Poznámka", max_length=255, null=True, blank=True
    )
    podpis = models.ImageField(
        verbose_name="Podpis", upload_to="podpisy", null=True, blank=True
    )

    class Meta:
        verbose_name = "TBD"
        verbose_name_plural = "TBD"


class PracovniNaklady(models.Model):
    rybnik = models.ForeignKey(Rybnik, on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Datum")
    cas = models.PositiveSmallIntegerField(verbose_name="Čas (hodiny)")
    popis_prace = models.CharField(verbose_name="Popis práce", max_length=255)
    najete_km = models.IntegerField(verbose_name="Najeté km")

    class Meta:
        verbose_name = "Pracovní náklady"
        verbose_name_plural = "Pracovní náklady"
