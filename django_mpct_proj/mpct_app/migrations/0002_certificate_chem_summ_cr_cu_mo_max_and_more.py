# Generated by Django 5.0 on 2024-02-07 10:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpct_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='chem_summ_cr_cu_mo_max',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cr+Cu+Mo'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='chem_summ_cr_mo_max',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cr+Mo'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='chem_summ_nb_ti_v_max',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nb+Ti+V'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='chem_summ_nb_v_max',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nb + V'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='chem_summ_ni_cr_mo_cu_max',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Ni+Cr+Mo+Cu'),
        ),
        migrations.AddField(
            model_name='material',
            name='chem_summ_cr_cu_mo_max',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cr+Cu+Mo'),
        ),
        migrations.AddField(
            model_name='material',
            name='chem_summ_cr_mo_max',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cr+Mo'),
        ),
        migrations.AddField(
            model_name='material',
            name='chem_summ_nb_ti_v_max',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nb+Ti+V'),
        ),
        migrations.AddField(
            model_name='material',
            name='chem_summ_nb_v_max',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nb + V'),
        ),
        migrations.AddField(
            model_name='material',
            name='chem_summ_ni_cr_mo_cu_max',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Ni+Cr+Mo+Cu'),
        ),
    ]