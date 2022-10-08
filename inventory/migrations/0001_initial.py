# Generated by Django 4.1.2 on 2022-10-08 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("quantity", models.FloatField()),
                ("unit_price", models.FloatField()),
                ("unit", models.CharField(max_length=30)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.AddIndex(
            model_name="ingredient",
            index=models.Index(fields=["name"], name="inventory_i_name_9e7294_idx"),
        ),
    ]