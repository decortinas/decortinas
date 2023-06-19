# Generated by Django 4.1.5 on 2023-04-26 14:48

from django.db import migrations, models
import storages.backends.gcloud


class Migration(migrations.Migration):

    dependencies = [
        ("productos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="productimg",
            field=models.ImageField(
                storage=storages.backends.gcloud.GoogleCloudStorage(),
                upload_to="uploads/",
                verbose_name="Imagen principal del Producto",
            ),
        ),
    ]