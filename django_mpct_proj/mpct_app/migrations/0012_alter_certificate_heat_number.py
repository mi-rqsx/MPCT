# Generated by Django 5.0 on 2023-12-14 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpct_app', '0011_certificate_chem_al_max_certificate_chem_al_min_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='heat_number',
            field=models.CharField(max_length=100),
        ),
    ]