# Generated by Django 5.0.1 on 2024-02-06 17:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_campaign_sale"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Sale",
        ),
    ]
