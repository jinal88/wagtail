# Generated by Django 5.1 on 2024-09-25 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0040_nocreatablesubpagetypespage_nosubpagetypespage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="jsonstreammodel",
            options={"verbose_name": "JSON stream model"},
        ),
    ]