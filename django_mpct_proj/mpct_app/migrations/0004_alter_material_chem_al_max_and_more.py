# Generated by Django 4.2.7 on 2023-11-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpct_app', '0003_remove_material_mech_toughness_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='chem_al_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Aluminum, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_al_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Aluminum, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_b_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Boron, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_b_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Boron, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_c_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Carbon, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_c_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Carbon, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_ca_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Calcium, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_ca_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Calcium, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_co_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Cobalt, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_co_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Cobalt, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_cr_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Chromium, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_cr_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Chromium, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_cu_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Copper, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_cu_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Copper, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_fe_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Iron, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_fe_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Iron, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_mn_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Manganese, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_mn_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Manganese, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_mo_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Molybdenum, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_mo_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Molybdenum, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_n_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Nitrogen, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_n_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Nitrogen, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_nb_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Niobium, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_nb_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Niobium, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_ni_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Nickel, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_ni_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Nickel, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_p_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Phosphorus, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_p_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Phosphorus, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_s_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Sulfur max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_s_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Sulfur min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_si_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Silicon, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_si_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_ti_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Titanium, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_ti_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Titanium, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_v_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Vanadium, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_v_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Vanadium, min'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_w_max',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Tungsten, max'),
        ),
        migrations.AlterField(
            model_name='material',
            name='chem_w_min',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Tungsten, min'),
        ),
    ]
