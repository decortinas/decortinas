# Generated by Django 4.1.5 on 2023-05-03 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productos", "0004_alter_product_productimg"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdditionalImage",
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
                (
                    "image",
                    models.ImageField(
                        upload_to="imagenes-decortinas/",
                        verbose_name="Imagen adicional del Producto",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="additional_images",
            field=models.ManyToManyField(blank=True, to="productos.additionalimage"),
        ),
    ]
