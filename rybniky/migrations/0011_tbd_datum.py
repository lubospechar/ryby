from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ("rybniky", "0010_rybnik_obec_rybnik_okres"),
    ]

    operations = [
        migrations.AddField(
            model_name="tbd",
            name="datum",
            field=models.DateTimeField(default=timezone.now, verbose_name="Datum a čas"),
            preserve_default=False,
        ),
    ]