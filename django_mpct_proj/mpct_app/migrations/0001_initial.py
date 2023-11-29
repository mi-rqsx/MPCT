# Generated by Django 4.2.7 on 2023-11-29 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chem_c_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Carbon')),
                ('chem_c_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_mn_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Manganese')),
                ('chem_mn_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_si_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Silicon')),
                ('chem_si_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_p_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Phosphorus')),
                ('chem_p_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_s_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Sulfur')),
                ('chem_s_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_ni_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Nickel')),
                ('chem_ni_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_cr_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Chromium')),
                ('chem_cr_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_cu_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Copper')),
                ('chem_cu_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_al_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Aluminum')),
                ('chem_al_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_v_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Vanadium')),
                ('chem_v_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_nb_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Niobium')),
                ('chem_nb_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_mo_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Molybdenum')),
                ('chem_mo_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_ti_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Titanium')),
                ('chem_ti_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_b_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Boron')),
                ('chem_b_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_n_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Nitrogen')),
                ('chem_n_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_ca_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Calcium')),
                ('chem_ca_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_co_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Cobalt')),
                ('chem_co_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_fe_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Iron')),
                ('chem_fe_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('chem_w_max', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Tungsten')),
                ('chem_w_min', models.DecimalField(decimal_places=4, max_digits=6)),
                ('mech_tensile_strength_max', models.IntegerField(verbose_name='TS, max')),
                ('mech_tensile_strength_min', models.IntegerField(verbose_name='TS, min')),
                ('mech_yield_strength_max', models.IntegerField(verbose_name='YS, max')),
                ('mech_yield_strength_min', models.IntegerField(verbose_name='YS, min')),
                ('mech_strength_units', models.CharField(choices=[('MPa', 'Megapascal'), ('PSI', 'Pounds per square inch'), ('KSI', 'Kilopounds per square inch')], default='MPa', max_length=20)),
                ('mech_hardness_max', models.IntegerField(verbose_name='Hardness, max')),
                ('mech_hardness_units', models.CharField(choices=[('HB', 'Brinell'), ('HV', 'Vickers'), ('HRC', 'Rockwell C'), ('HRB', 'Rockwell B'), ('HRA', 'Rockwell A')], default='HB', max_length=20)),
                ('mech_toughness_1', models.IntegerField(verbose_name='Impact test')),
                ('mech_toughness_2', models.IntegerField()),
                ('mech_toughness_3', models.IntegerField()),
                ('mech_toughness_units', models.CharField(choices=[('J', 'Joule')], default='J', max_length=20)),
                ('mech_toughness_size', models.CharField(choices=[('10x10', '10x10'), ('7.5x10', '7.5x10'), ('5x10', '5x10'), ('2.5x10', '2.5x10')], default='10x10', max_length=20)),
                ('grade', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, max_length=100, null=True, verbose_name='Class or Category')),
                ('material_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mpct_app.materialtype')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mpct_app.specifications')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
